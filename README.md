# cookiecutter-agentic-python

Cookiecutter template for a **Python** project set up for **agentic coding with Cline**.

It encodes 2026 agent-file practice (lean `AGENTS.md`, Cline `.clinerules/`, progressive disclosure) and a small layered `src` layout that stays maintainable as the project grows.

## Generate a project

```bash
# one-shot, no install
uvx cookiecutter /path/to/cookiecutter-agentic-python

# or from this folder
cd cookiecutter-agentic-python
uvx cookiecutter .
```

Then:

```bash
cd <project_slug>
uv sync
uv run pytest
uv run ruff check .
```

Open the new folder in VS Code and start Cline. It will pick up `AGENTS.md` and `.clinerules/`.

## What you get

| Piece | Why it exists |
| --- | --- |
| `AGENTS.md` | Always-loaded, short operating manual (~100 lines). Commands first. |
| `.clinerules/` | Cline-native rules split by topic so you can add sprint notes without bloating the root file. |
| `.agents/docs/` | Detail Cline should open *only when the task needs it*. |
| `src/<package>/{domain,services,adapters}` | Default layering for logical, testable code. Delete a layer if you do not need it. |
| `uv` + Ruff + pytest + ty | Fast, modern quality gates the agent can actually run. |
| `docs/adr/` | Architecture Decision Records when a choice should outlive a chat. |

## Design rules baked into the template

- Keep the always-loaded agent file short. Long rule files get ignored.
- Prefer the smallest correct change. Do not rewrite for taste.
- Domain logic has no I/O. Adapters talk to files, APIs, Excel, databases.
- Do not claim tests passed unless they were run.
- When the agent gets something wrong twice, add a rule — or a test.

See the generated project's `README.md` and `.agents/docs/` for the rest.
