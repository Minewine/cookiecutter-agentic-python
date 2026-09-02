# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Python {{ cookiecutter.python_version }} · Cline-ready · `uv` + Ruff + pytest

## Setup

```bash
uv sync
cp .env.example .env   # then edit
uv run pytest
```

{% if cookiecutter.include_cli == "y" %}
```bash
uv run {{ cookiecutter.project_slug }} Ada
```
{% endif %}

## Layout

```
src/{{ cookiecutter.package_name }}/
  domain/      # rules and types — no I/O
  services/    # use cases
  adapters/    # files, APIs, Excel, stdout
tests/
AGENTS.md      # what Cline loads every session
.clinerules/   # Cline-native extras
.agents/docs/  # read on demand
docs/adr/      # decisions
```

## Agent workflow

1. Open the repo in VS Code with Cline.
2. Use Plan mode for multi-file work.
3. Point Cline at `AGENTS.md`. It will follow commands there.
4. After a repeated miss, add a line to `.clinerules/` or a test.

Quality gate:

```bash
bash scripts/check.sh
```

## Maintainability defaults

- Smallest correct change.
- Domain does not import adapters.
- New behaviour needs a test that would have failed before.
- New libraries and structural shifts get an ADR.

Read `.agents/docs/architecture.md` before inventing a new folder.
