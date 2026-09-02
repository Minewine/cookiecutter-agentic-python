# {{ cookiecutter.project_name }}

Python {{ cookiecutter.python_version }} package `{{ cookiecutter.package_name }}`.
{{ cookiecutter.description }}

Primary agent: **Cline**. Keep this file short. Read linked docs only when the task needs them.

## Commands

```bash
uv sync
uv run pytest
uv run pytest tests/test_architecture.py
uv run pytest tests/path/test_file.py -k name -q
uv run ruff check --fix .
uv run ruff format .
uv run ty check
```

A task is done only when the checks that apply have been run, not guessed.

## Layout

```
src/{{ cookiecutter.package_name }}/
  domain/      # pure logic: no files, network, Excel, DB
  services/    # use-cases that orchestrate domain + adapters
  adapters/    # I/O: APIs, CSV/XLSX, filesystem, HTTP
tests/         # mirrors src
.agents/docs/  # long-form guidance — open on demand
docs/adr/      # decisions that should outlive a chat
```

Do not invent a new top-level package. Grow inside these layers. Delete a layer you do not use.

## Defaults

- Smallest correct change. Do not rewrite a file to change one function.
- Restate the task in one sentence before editing more than one file.
- Ask if the request becomes a redesign, deletes data, or needs a new dependency.
- Do not invent APIs, columns, config keys, or test results.
- Do not edit unrelated files "while you are here".
- Secrets stay in `.env` (never committed). Use `.env.example` as the contract.

## Code

- Type-hint public functions, including return types.
- Use `pathlib.Path`. No `os.path`.
- Raise specific exceptions from `{{ cookiecutter.package_name }}.domain.errors`.
- Domain functions are deterministic and unit-tested.
- I/O lives in adapters. Services wire them. Domain does not import adapters or services.

## Read when needed

- Before writing or reshaping modules: `.agents/docs/architecture.md`
- Style and naming: `.agents/docs/coding-guidelines.md`
- Tests: `.agents/docs/testing.md`
- Prior choices: `docs/adr/` and `.agents/docs/decisions.md`
- Recurring bugs: `.agents/docs/known-issues.md`
- Cline + z.ai / GLM: `.clinerules/00-zai-glm.md`

## After a miss

If the user had to correct you, or the same mistake happened twice, add one concrete line to `.clinerules/` or a failing test — not a paragraph of philosophy.
