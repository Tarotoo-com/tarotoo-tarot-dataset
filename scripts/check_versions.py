"""Fail if the version is not identical everywhere it is declared.

Two releases' worth of drift went unnoticed once: the published 2.0.0 PyPI package
reported __version__ == "1.7.1" and CITATION.cff still cited 1.7.1. Run in CI.

    python3 scripts/check_versions.py
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def found() -> dict[str, str]:
    out: dict[str, str] = {}
    out["packages/npm/package.json"] = json.loads(
        (ROOT / "packages/npm/package.json").read_text())["version"]
    out["packages/python/pyproject.toml"] = tomllib.loads(
        (ROOT / "packages/python/pyproject.toml").read_text())["project"]["version"]
    cff = re.search(r"^version:\s*(\S+)\s*$",
                    (ROOT / "CITATION.cff").read_text(), re.M)
    out["CITATION.cff"] = cff.group(1) if cff else "MISSING"
    # A literal __version__ would be drift waiting to happen; the package reads its
    # own metadata instead, so only its source-checkout fallback is checked here.
    init = (ROOT / "packages/python/src/tarotoo_tarot/__init__.py").read_text()
    literal = re.search(r'__version__\s*=\s*"([^"]+)"', init)
    fallback = re.search(r'PackageNotFoundError.*?\n\s*__version__\s*=\s*"([^"]+)"',
                         init, re.S)
    if fallback:
        out["python fallback"] = fallback.group(1)
    elif literal:
        out["python __version__ (hardcoded)"] = literal.group(1)
    return out


def main() -> int:
    versions = found()
    for where, v in sorted(versions.items()):
        print(f"  {v:10} {where}")
    unique = set(versions.values())
    if len(unique) != 1:
        print(f"\nFAIL: {len(unique)} different versions declared: {sorted(unique)}")
        return 1
    print(f"\nOK: everything declares {unique.pop()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
