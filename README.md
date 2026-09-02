# cookiecutter-agentic-python

Cookiecutter template for a **Python** project set up for **agentic coding with Cline**.

It encodes 2026 agent-file practice (lean `AGENTS.md`, Cline `.clinerules/`, progressive disclosure) and a small layered `src` layout that stays maintainable as the project grows.

## Generate a project

```bash
# from GitHub — replace OWNER with your GitHub user or org
uvx cookiecutter gh:OWNER/cookiecutter-agentic-python

# from a local clone
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
| `.clinerules/00-zai-glm.md` | Known-good Cline + z.ai / GLM profile (provider URL, short prompts). |
| `.clinerules/` | Other Cline rules split by topic. |
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

CI on this repo generates a child project and runs its tests (`template` workflow). Meta-checks fail if `AGENTS.md` exceeds 150 lines, required headings are missing, or `domain` imports `adapters`.

```bash
pip install cookiecutter
python scripts/check_template.py
```

See **[USER_GUIDE.md](USER_GUIDE.md)** for Cline + z.ai setup, the daily loop, and how to grow rules.
