"""Add src/ to sys.path so EverOS package is importable in all lib tests."""
from __future__ import annotations

import sys
from pathlib import Path

src = str(Path(__file__).parent.parent.parent / "src")
if src not in sys.path:
    sys.path.insert(0, src)
