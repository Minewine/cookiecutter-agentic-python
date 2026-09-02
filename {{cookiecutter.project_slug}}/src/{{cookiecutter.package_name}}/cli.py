"""Minimal CLI. Delete this file if you generated the project without a CLI."""

from __future__ import annotations

import argparse
import sys

from {{ cookiecutter.package_name }}.adapters.stdout import write_stdout
from {{ cookiecutter.package_name }}.domain.errors import DomainError
from {{ cookiecutter.package_name }}.services.run_greeting import run_greeting


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.project_slug }}")
    parser.add_argument("name", help="Name to greet")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        run_greeting(args.name, write_stdout)
    except DomainError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
