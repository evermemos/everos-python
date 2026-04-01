"""Multimodal add orchestration: detect → resolve → batch sign → concurrent upload → replace uri → add.

MemoriesResourceWithMultimodal overrides add() while keeping the same signature.
The user calls client.v1.memories.add() exactly as before; the SDK handles uploads transparently.
"""

from __future__ import annotations

import os
import copy
import logging
from typing import Any, List, Iterable, Optional, cast
from typing_extensions import override
from concurrent.futures import Future, ThreadPoolExecutor, as_completed

import httpx

from ._files import FileInput, ResolvedFile, resolve_file, async_resolve_file
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ._detect import UploadTask, scan_messages
from ._errors import MultimodalError, FileResolveError
from ._upload import SignedFile, UploadResult, batch_sign, s3_post_upload, async_batch_sign, async_s3_post_upload
from ..types.v1.add_response import AddResponse
from ..types.v1.message_item_param import MessageItemParam
from ..resources.v1.memories.memories import MemoriesResource, AsyncMemoriesResource

log: logging.Logger = logging.getLogger("everos")

_DEFAULT_MAX_WORKERS = 4


# ── Sync resource override ────────────────────────────────────────────────────


class MemoriesResourceWithMultimodal(MemoriesResource):
    """Inherits MemoriesResource and overrides add() with transparent multimodal upload."""

    @override
    def add(
        self,
        *,
        messages: Iterable[MessageItemParam],
        user_id: str,
        async_mode: bool | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """add() with automatic multimodal upload.

        Scans content items in each message:
        - uri is a local file path → sign + upload → replace with object_key
        - uri is an http(s) URL   → download → sign + upload → replace with object_key
        - uri is already an object_key (or any other value) → pass through unchanged

        Signature is identical to the generated add().
        """
        msg_list = _materialise(messages)
        upload_tasks = scan_messages(msg_list)

        if not upload_tasks:
            log.debug("No uploadable content detected, passing through to add()")
            return super().add(
                messages=cast(Iterable[MessageItemParam], msg_list),
                user_id=user_id, async_mode=async_mode,
                session_id=session_id, extra_headers=extra_headers,
                extra_query=extra_query, extra_body=extra_body, timeout=timeout,
            )

        log.debug("Multimodal detected: %d file(s) to upload", len(upload_tasks))
        for i, t in enumerate(upload_tasks):
            log.debug(
                "  [%d] messages[%d].content[%d] type=%s uri=%s (%s)",
                i, t.msg_idx, t.content_idx, t.content_type, t.uri, t.uri_type,
            )

        msg_list = copy.deepcopy(msg_list)
        resolved_files: List[ResolvedFile] = []

        try:
            _resolve_all(upload_tasks, resolved_files)
            signed_files = batch_sign(self._client, upload_tasks, resolved_files)
            results = _concurrent_upload(signed_files, upload_tasks)
            _replace_uris(msg_list, upload_tasks, results)
            log.debug("Multimodal upload complete: %d file(s), calling add()", len(upload_tasks))
            return super().add(
                messages=cast(Iterable[MessageItemParam], msg_list),
                user_id=user_id, async_mode=async_mode,
                session_id=session_id, extra_headers=extra_headers,
                extra_query=extra_query, extra_body=extra_body, timeout=timeout,
            )

        finally:
            _cleanup(resolved_files)


# ── Async resource override ───────────────────────────────────────────────────


class AsyncMemoriesResourceWithMultimodal(AsyncMemoriesResource):
    """Async version — mirrors MemoriesResourceWithMultimodal."""

    @override
    async def add(
        self,
        *,
        messages: Iterable[MessageItemParam],
        user_id: str,
        async_mode: bool | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """Async add() with automatic multimodal upload. Signature identical to generated add()."""
        msg_list = _materialise(messages)
        upload_tasks = scan_messages(msg_list)

        if not upload_tasks:
            log.debug("No uploadable content detected, passing through to add() (async)")
            return await super().add(
                messages=cast(Iterable[MessageItemParam], msg_list),
                user_id=user_id, async_mode=async_mode,
                session_id=session_id, extra_headers=extra_headers,
                extra_query=extra_query, extra_body=extra_body, timeout=timeout,
            )

        log.debug("Multimodal detected: %d file(s) to upload (async)", len(upload_tasks))

        msg_list = copy.deepcopy(msg_list)
        resolved_files: List[ResolvedFile] = []

        try:
            await _async_resolve_all(upload_tasks, resolved_files)
            signed_files = await async_batch_sign(self._client, upload_tasks, resolved_files)
            results = await _async_concurrent_upload(signed_files, upload_tasks)
            _replace_uris(msg_list, upload_tasks, results)
            log.debug("Multimodal upload complete: %d file(s), calling add() (async)", len(upload_tasks))
            return await super().add(
                messages=cast(Iterable[MessageItemParam], msg_list),
                user_id=user_id, async_mode=async_mode,
                session_id=session_id, extra_headers=extra_headers,
                extra_query=extra_query, extra_body=extra_body, timeout=timeout,
            )

        finally:
            _cleanup(resolved_files)


# ── Shared helpers ────────────────────────────────────────────────────────────


def _materialise(messages: Iterable[MessageItemParam]) -> list[dict[str, Any]]:
    """Convert iterable of messages to list[dict] for scanning and mutation."""
    return [dict(m) if isinstance(m, dict) else m for m in messages]  # type: ignore[misc]


def _resolve_all(upload_tasks: List[UploadTask], resolved_files: List[ResolvedFile]) -> None:
    """Resolve files sequentially (preserves order)."""
    for task in upload_tasks:
        try:
            fi = FileInput(path=task.uri) if task.uri_type == "local" else FileInput(url=task.uri)
            resolved_files.append(resolve_file(fi))
            log.debug(
                "Resolved %s → %d bytes %s",
                task.uri, resolved_files[-1].size, resolved_files[-1].content_type,
            )
        except FileResolveError:
            raise
        except Exception as exc:
            raise FileResolveError(
                f"Failed to resolve messages[{task.msg_idx}].content[{task.content_idx}] "
                f"(uri={task.uri}): {exc}"
            ) from exc


async def _async_resolve_all(
    upload_tasks: List[UploadTask], resolved_files: List[ResolvedFile]
) -> None:
    """Async parallel resolve (preserves order via gather).

    On failure, cleans up ALL already-resolved temp files (both those appended to
    resolved_files and those only present in the gather results list).
    """
    import asyncio

    async def _resolve_one(task: UploadTask) -> ResolvedFile:
        fi = FileInput(path=task.uri) if task.uri_type == "local" else FileInput(url=task.uri)
        return await async_resolve_file(fi)

    coros = [_resolve_one(t) for t in upload_tasks]
    results = await asyncio.gather(*coros, return_exceptions=True)

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            # Clean up ALL resolved temp files: those already appended AND those
            # only present in results (gather ran them concurrently).
            for r in results:
                if isinstance(r, ResolvedFile):
                    r.cleanup()
            task = upload_tasks[i]
            raise FileResolveError(
                f"Failed to resolve messages[{task.msg_idx}].content[{task.content_idx}] "
                f"(uri={task.uri}): {result}"
            ) from result
        resolved_files.append(result)  # type: ignore[arg-type]
        log.debug("Resolved %s → %d bytes", upload_tasks[i].uri, result.size)  # type: ignore[union-attr]


def _concurrent_upload(
    signed_files: List[SignedFile],
    upload_tasks: List[UploadTask],
    max_workers: int = _DEFAULT_MAX_WORKERS,
) -> List[UploadResult]:
    """Upload files concurrently (order-preserving, best-effort fail-fast).

    On the first upload failure, cancels futures not yet started. Futures already
    running cannot be interrupted; the ThreadPoolExecutor context manager blocks
    until they complete before this function returns.
    """
    n = len(signed_files)
    results: List[UploadResult | None] = [None] * n

    with ThreadPoolExecutor(max_workers=min(max_workers, n)) as executor:
        future_to_idx: dict[Future[UploadResult], int] = {}
        futures: list[Future[UploadResult]] = []
        for i, sf in enumerate(signed_files):
            fut = executor.submit(s3_post_upload, sf)
            futures.append(fut)
            future_to_idx[fut] = i

        first_error: Exception | None = None
        first_error_idx = -1

        for fut in as_completed(future_to_idx):
            idx = future_to_idx[fut]
            try:
                results[idx] = fut.result()
            except Exception as exc:
                first_error = exc
                first_error_idx = idx
                for other in futures:
                    if other is not fut:
                        other.cancel()
                break

        if first_error is not None:
            task = upload_tasks[first_error_idx]
            raise MultimodalError(
                f"Upload failed at messages[{task.msg_idx}].content[{task.content_idx}] "
                f"(uri={task.uri}): {first_error}"
            ) from first_error

    return results  # type: ignore[return-value]


async def _async_concurrent_upload(
    signed_files: List[SignedFile],
    upload_tasks: List[UploadTask],
) -> List[UploadResult]:
    """Async concurrent upload (order-preserving, fail-fast via FIRST_EXCEPTION).

    When FIRST_EXCEPTION fires, all tasks in `done` are already finished.
    With no error, pending is always empty (asyncio.wait returns all in done).
    """
    import asyncio

    n = len(signed_files)
    results: List[UploadResult | None] = [None] * n
    task_to_idx: dict[asyncio.Task[UploadResult], int] = {}
    async_tasks: list[asyncio.Task[UploadResult]] = []

    for i, sf in enumerate(signed_files):
        t = asyncio.create_task(async_s3_post_upload(sf), name=f"upload-{i}")
        async_tasks.append(t)
        task_to_idx[t] = i

    done, pending = await asyncio.wait(async_tasks, return_when=asyncio.FIRST_EXCEPTION)

    first_error: BaseException | None = None
    first_error_idx = -1

    for t in done:
        idx = task_to_idx[t]
        exc = t.exception()
        if exc is not None:
            if first_error is None or idx < first_error_idx:
                first_error = exc
                first_error_idx = idx
        else:
            results[idx] = t.result()

    if first_error is not None:
        for t in pending:
            t.cancel()
        if pending:
            done_after_cancel, _ = await asyncio.wait(pending)
            # Consume exceptions to suppress unobserved-exception warnings (Python 3.11+)
            for t in done_after_cancel:
                if not t.cancelled():
                    t.exception()
        task = upload_tasks[first_error_idx]
        raise MultimodalError(
            f"Upload failed at messages[{task.msg_idx}].content[{task.content_idx}]: {first_error}"
        ) from first_error  # type: ignore[arg-type]

    # No error: pending is always empty when FIRST_EXCEPTION returns all tasks done.
    # (Defensive guard kept for clarity, but unreachable in practice.)
    assert not pending, "unexpected pending tasks after FIRST_EXCEPTION with no error"

    return results  # type: ignore[return-value]


def _replace_uris(
    msg_list: list[dict[str, Any]],
    upload_tasks: List[UploadTask],
    results: List[UploadResult],
) -> None:
    """Replace uri in each content item with the uploaded object_key."""
    for i, task in enumerate(upload_tasks):
        result = results[i]
        content_item = msg_list[task.msg_idx]["content"][task.content_idx]
        log.debug(
            "Replaced messages[%d].content[%d].uri: %s → %s",
            task.msg_idx, task.content_idx, task.uri, result.object_key,
        )
        content_item["uri"] = result.object_key
        # auto-fill name and ext if absent
        if not content_item.get("name") and result.filename:
            content_item["name"] = result.filename
        if not content_item.get("ext") and result.filename:
            ext = os.path.splitext(result.filename)[1].lstrip(".")
            if ext:
                content_item["ext"] = ext


def _cleanup(resolved_files: List[ResolvedFile]) -> None:
    """Clean up temp files. Always called from finally blocks."""
    cleaned = 0
    for r in resolved_files:
        if r.is_temp:
            r.cleanup()
            cleaned += 1
    if cleaned:
        log.debug("Cleaned up %d temp file(s)", cleaned)
