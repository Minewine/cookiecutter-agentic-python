"""Guardrails the agent can run locally: domain stays free of I/O layers."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
FORBIDDEN_PARTS = frozenset({"adapters", "services"})


def _domain_dirs() -> list[Path]:
    found = sorted(p for p in SRC.glob("*/domain") if p.is_dir())
    if not found:
        raise AssertionError(f"no src/<package>/domain directory under {SRC}")
    return found


def _forbidden_imports(tree: ast.AST) -> list[str]:
    hits: list[str] = []
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                names.append(node.module)
            if node.level >= 2 and (not node.module or node.module.split(".")[0] in FORBIDDEN_PARTS):
                names.append(node.module or next(iter(FORBIDDEN_PARTS)))
        for name in names:
            first = name.split(".")[0]
            last = name.split(".")[-1]
            if first in FORBIDDEN_PARTS or last in FORBIDDEN_PARTS:
                hits.append(name)
            if any(part in FORBIDDEN_PARTS for part in name.split(".")):
                if name not in hits:
                    hits.append(name)
    return hits


def test_domain_does_not_import_adapters_or_services() -> None:
    checked = 0
    for domain in _domain_dirs():
        for py in domain.rglob("*.py"):
            checked += 1
            tree = ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
            hits = _forbidden_imports(tree)
            assert not hits, f"{py} imports a forbidden layer: {hits}"
    assert checked > 0
