#!/usr/bin/env bash
set -euo pipefail
uv run ruff check --fix .
uv run ruff format .
uv run pytest
uv run ty check || true
