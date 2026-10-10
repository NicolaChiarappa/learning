"""Hidden edge-case tests. Assessor only.

Run from the test folder root:
    .venv/bin/pytest _assessor -v
Set ASSESS_SOLUTIONS_DIR to point to another directory with the same
exercise sub-folders (used to validate these tests against a reference).
"""
import os
import sys
from pathlib import Path

_default = Path(__file__).resolve().parent.parent / "04-scrittura-codice"
_base = Path(os.environ.get("ASSESS_SOLUTIONS_DIR", _default))
for sub in sorted(_base.iterdir()):
    if sub.is_dir():
        sys.path.insert(0, str(sub))
