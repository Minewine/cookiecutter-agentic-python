#!/usr/bin/env python3
"""Meta-checks for the cookiecutter and for a generated project.

Usage:
  python scripts/check_template.py
  python scripts/check_template.py --project /tmp/my-project
"""

from __future__ import annotations

import argparse
import ast
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_AGENTS_LINES = 150
REQUIRED_HEADINGS = ("Commands", "Layout", "Defaults")
DOMAIN_IMPORT_BAN = re.compile(
    r"^\s*(from|import)\s+(\.\.adapters|[\w.]+\.adapters)\b",
    re.MULTILINE,
)


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def check_agents_md(path: Path) -> None:
    if not path.is_file():
        fail(f"missing {path}")
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > MAX_AGENTS_LINES:
        fail(f"{path} has {len(lines)} lines; cap is {MAX_AGENTS_LINES}")
    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE):
            fail(f"{path} missing heading ## {heading}")
    print(f"OK  AGENTS.md ({len(lines)} lines) {path}")


def _imports_adapters(tree: ast.AST) -> list[str]:
    hits: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "adapters" or alias.name.endswith(".adapters"):
                    hits.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if mod == "adapters" or mod.endswith(".adapters") or mod.startswith("adapters."):
                hits.append(mod)
            if node.level >= 2 and (mod == "adapters" or mod.startswith("adapters")):
                hits.append(mod or "adapters")
    return hits


def check_domain_does_not_import_adapters(src_root: Path) -> None:
    domain_dirs = list(src_root.glob("*/domain")) + list(src_root.glob("domain"))
    if src_root.name == "src":
        domain_dirs = list(src_root.glob("*/domain"))
    if not domain_dirs:
        fail(f"no domain/ package under {src_root}")
    checked = 0
    for domain in domain_dirs:
        for py in domain.rglob("*.py"):
            checked += 1
            source = py.read_text(encoding="utf-8")
            if DOMAIN_IMPORT_BAN.search(source):
                fail(f"{py} looks like it imports adapters")
            try:
                tree = ast.parse(source, filename=str(py))
            except SyntaxError as exc:
                fail(f"{py} is not valid Python: {exc}")
            hits = _imports_adapters(tree)
            if hits:
                fail(f"{py} imports adapters: {hits}")
    print(f"OK  domain import rule ({checked} files) {src_root}")


def check_zai_profile(project: Path) -> None:
    path = project / ".clinerules" / "00-zai-glm.md"
    if not path.is_file():
        fail(f"missing {path}")
    text = path.read_text(encoding="utf-8").lower()
    for needle in ("z.ai", "glm", "base url", "uv run pytest"):
        if needle not in text:
            fail(f"{path} missing {needle!r}")
    print(f"OK  z.ai profile {path}")


def generate_project(dest: Path) -> Path:
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "cookiecutter",
            str(ROOT),
            "--no-input",
            "-o",
            str(dest),
        ],
        check=True,
    )
    children = [p for p in dest.iterdir() if p.is_dir()]
    if len(children) != 1:
        fail(f"expected one generated project in {dest}, got {children}")
    return children[0]


def check_project(project: Path) -> None:
    check_agents_md(project / "AGENTS.md")
    check_zai_profile(project)
    src = project / "src"
    if not src.is_dir():
        fail(f"missing {src}")
    check_domain_does_not_import_adapters(src)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, help="Already-generated project to check")
    args = parser.parse_args()

    template_agents = ROOT / "{{cookiecutter.project_slug}}" / "AGENTS.md"
    check_agents_md(template_agents)

    if args.project:
        check_project(args.project)
        return

    try:
        import cookiecutter  # noqa: F401
    except ImportError:
        print("skip generate: cookiecutter not installed (pip install cookiecutter)")
        return

    with tempfile.TemporaryDirectory() as tmp:
        project = generate_project(Path(tmp))
        check_project(project)


if __name__ == "__main__":
    main()
