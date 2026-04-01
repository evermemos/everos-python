"""Multimodal upload exceptions."""

from __future__ import annotations


class MultimodalError(Exception):
    """Base exception for multimodal upload operations."""
    pass


class FileResolveError(MultimodalError):
    """Failed to resolve a file input (path not found, URL download failure, size exceeded, etc.)."""
    pass


class UploadError(MultimodalError):
    """Failed to sign or upload a file to S3."""
    pass
