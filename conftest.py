"""pytest path setup for the external plugins repo.

The plugin payloads import as ``plugins.<name>`` (the same shape the core
uses), so the repo root must be on ``sys.path`` before the tests run.
The slave-agent core itself is a normal installed dependency (pip /
``PYTHONPATH`` pointing at a core checkout) — this file only arranges
THIS repo's layout.
"""
import sys
from pathlib import Path

_ROOT = str(Path(__file__).resolve().parent)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
