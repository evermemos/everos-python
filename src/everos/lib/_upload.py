"""Batch sign + S3 POST form upload.

One call to object.sign() signs all files; then each file is uploaded via S3
presigned POST (multipart/form-data with policy fields + file).
"""

from __future__ import annotations

import time
import uuid
import asyncio
from typing import TYPE_CHECKING, List
from dataclasses import dataclass

import httpx

from ._files import ResolvedFile
from ._detect import UploadTask
from ._errors import UploadError

if TYPE_CHECKING:
    from .._client import EverOS, AsyncEverOS

import logging

log: logging.Logger = logging.getLogger("everos")

_UPLOAD_TIMEOUT = 120.0
_MAX_UPLOAD_RETRIES = 3
_RETRY_BACKOFF_S = 1.0  # seconds to sleep between S3 upload retries


@dataclass
class SignedFile:
    """Holds sign response data for a single file, ready for upload."""

    resolved: ResolvedFile
    task: UploadTask
    object_key: str
    upload_url: str
    upload_fields: dict[str, str]


@dataclass
class UploadResult:
    """Result of a single successful upload."""

    object_key: str
    filename: str
    content_type: str
    size: int


# ── Sync ──────────────────────────────────────────────────────────────────────


def batch_sign(
    client: EverOS,
    upload_tasks: List[UploadTask],
    resolved_files: List[ResolvedFile],
) -> List[SignedFile]:
    """Sign all files in a single API call. Sign uses SDK built-in retry."""
    object_list = [
        {
            "file_id": f"sdk-{uuid.uuid4().hex}",
            "file_name": resolved.filename,
            "file_type": task.file_type,
        }
        for task, resolved in zip(upload_tasks, resolved_files)
    ]

    log.debug("Signing %d file(s) in one batch request", len(object_list))
    sign_resp = client.v1.object.sign(object_list=object_list)  # type: ignore[arg-type]

    if sign_resp.status != 0 or sign_resp.error != "OK":
        raise UploadError(
            f"Sign failed: status={sign_resp.status}, error={sign_resp.error}"
        )

    items = sign_resp.result.data.object_list if (sign_resp.result and sign_resp.result.data) else []
    if not items or len(items) != len(upload_tasks):
        raise UploadError(
            f"Sign returned {len(items or [])} items, expected {len(upload_tasks)}"
        )

    signed_files: list[SignedFile] = []
    for i, item in enumerate(items):
        if not item.object_key or not item.object_signed_info or not item.object_signed_info.url:
            raise UploadError(f"Sign response item {i} is missing object_key or upload_url")
        log.debug("  Signed: %s → %s", resolved_files[i].filename, item.object_key)
        signed_files.append(SignedFile(
            resolved=resolved_files[i],
            task=upload_tasks[i],
            object_key=item.object_key,
            upload_url=item.object_signed_info.url,
            upload_fields=dict(item.object_signed_info.fields or {}),
        ))
    return signed_files


def s3_post_upload(signed: SignedFile) -> UploadResult:
    """Upload a single file via S3 presigned POST form. Retries on 5xx / timeout."""
    resolved = signed.resolved
    last_error: Exception | None = None

    for attempt in range(_MAX_UPLOAD_RETRIES):
        try:
            log.debug(
                "Uploading %s (%s bytes) to S3 (attempt %d/%d)",
                resolved.filename, resolved.size, attempt + 1, _MAX_UPLOAD_RETRIES,
            )
            with resolved.open() as fh:
                resp = httpx.post(
                    signed.upload_url,
                    data=signed.upload_fields,
                    files={"file": (resolved.filename, fh, resolved.content_type)},
                    timeout=_UPLOAD_TIMEOUT,
                )

            if resp.status_code in (200, 201, 204):
                log.debug("Uploaded %s → HTTP %d", resolved.filename, resp.status_code)
                return UploadResult(
                    object_key=signed.object_key,
                    filename=resolved.filename,
                    content_type=resolved.content_type,
                    size=resolved.size,
                )

            if resp.status_code < 500:
                raise UploadError(
                    f"S3 upload failed (HTTP {resp.status_code}): {resp.text[:400]}"
                )

            last_error = UploadError(f"S3 server error: HTTP {resp.status_code}")
            log.warning(
                "S3 upload retry %d/%d for %s: HTTP %d",
                attempt + 1, _MAX_UPLOAD_RETRIES, resolved.filename, resp.status_code,
            )

        except httpx.TimeoutException as exc:
            last_error = exc
            log.warning(
                "S3 upload retry %d/%d for %s: timeout",
                attempt + 1, _MAX_UPLOAD_RETRIES, resolved.filename,
            )

        if attempt < _MAX_UPLOAD_RETRIES - 1:
            time.sleep(_RETRY_BACKOFF_S)

    raise UploadError(
        f"S3 upload failed after {_MAX_UPLOAD_RETRIES} attempts for {resolved.filename}"
    ) from last_error


# ── Async ─────────────────────────────────────────────────────────────────────


async def async_batch_sign(
    client: AsyncEverOS,
    upload_tasks: List[UploadTask],
    resolved_files: List[ResolvedFile],
) -> List[SignedFile]:
    """Async batch sign — mirrors sync version."""
    object_list = [
        {
            "file_id": f"sdk-{uuid.uuid4().hex}",
            "file_name": resolved.filename,
            "file_type": task.file_type,
        }
        for task, resolved in zip(upload_tasks, resolved_files)
    ]

    log.debug("Signing %d file(s) in one batch request (async)", len(object_list))
    sign_resp = await client.v1.object.sign(object_list=object_list)  # type: ignore[arg-type]

    if sign_resp.status != 0 or sign_resp.error != "OK":
        raise UploadError(
            f"Sign failed: status={sign_resp.status}, error={sign_resp.error}"
        )

    items = sign_resp.result.data.object_list if (sign_resp.result and sign_resp.result.data) else []
    if not items or len(items) != len(upload_tasks):
        raise UploadError(
            f"Sign returned {len(items or [])} items, expected {len(upload_tasks)}"
        )

    signed_files: list[SignedFile] = []
    for i, item in enumerate(items):
        if not item.object_key or not item.object_signed_info or not item.object_signed_info.url:
            raise UploadError(f"Sign response item {i} is missing object_key or upload_url")
        log.debug("  Signed: %s → %s", resolved_files[i].filename, item.object_key)
        signed_files.append(SignedFile(
            resolved=resolved_files[i],
            task=upload_tasks[i],
            object_key=item.object_key,
            upload_url=item.object_signed_info.url,
            upload_fields=dict(item.object_signed_info.fields or {}),
        ))
    return signed_files


async def async_s3_post_upload(signed: SignedFile) -> UploadResult:
    """Async S3 POST upload with retry."""
    import anyio

    resolved = signed.resolved
    last_error: Exception | None = None

    for attempt in range(_MAX_UPLOAD_RETRIES):
        try:
            log.debug(
                "Uploading %s (%s bytes) to S3 async (attempt %d/%d)",
                resolved.filename, resolved.size, attempt + 1, _MAX_UPLOAD_RETRIES,
            )
            fh = await anyio.to_thread.run_sync(resolved.open)  # type: ignore[attr-defined]
            try:
                async with httpx.AsyncClient(timeout=_UPLOAD_TIMEOUT) as http:
                    resp = await http.post(
                        signed.upload_url,
                        data=signed.upload_fields,
                        files={"file": (resolved.filename, fh, resolved.content_type)},  # type: ignore[arg-type]
                    )
            finally:
                await anyio.to_thread.run_sync(fh.close)  # type: ignore[attr-defined]

            if resp.status_code in (200, 201, 204):
                log.debug("Uploaded %s → HTTP %d", resolved.filename, resp.status_code)
                return UploadResult(
                    object_key=signed.object_key,
                    filename=resolved.filename,
                    content_type=resolved.content_type,
                    size=resolved.size,
                )

            if resp.status_code < 500:
                raise UploadError(
                    f"S3 upload failed (HTTP {resp.status_code}): {resp.text[:400]}"
                )

            last_error = UploadError(f"S3 server error: HTTP {resp.status_code}")
            log.warning(
                "S3 upload retry %d/%d for %s: HTTP %d",
                attempt + 1, _MAX_UPLOAD_RETRIES, resolved.filename, resp.status_code,
            )

        except httpx.TimeoutException as exc:
            last_error = exc
            log.warning(
                "S3 upload retry %d/%d for %s: timeout",
                attempt + 1, _MAX_UPLOAD_RETRIES, resolved.filename,
            )

        if attempt < _MAX_UPLOAD_RETRIES - 1:
            await asyncio.sleep(_RETRY_BACKOFF_S)

    raise UploadError(
        f"S3 upload failed after {_MAX_UPLOAD_RETRIES} attempts for {resolved.filename}"
    ) from last_error
