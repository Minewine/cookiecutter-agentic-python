# Agentic development user guide

How to use this cookiecutter with **Cline** and **z.ai (GLM)** so the agent produces logical, maintainable Python.

This file is meant to live in the template repository.

## Two directories

| Thing | Typical path | Role |
| --- | --- | --- |
| Template | `~/Projects/cookiecutter-agentic-python` | Cookiecutter source. This guide lives here. |
| Generated app | `~/Projects/<project-slug>` | Real project Cline edits. Gets its own `AGENTS.md`. |

The folder named `{{cookiecutter.project_slug}}` inside the template is not broken. Cookiecutter replaces that name when you generate a project.

## Tooling

- VS Code + [Cline](https://cline.bot)
- [z.ai](https://z.ai) API key (GLM coding plan or pay-as-you-go)
- [uv](https://docs.astral.sh/uv/)
- Git

### Point Cline at z.ai

In Cline: **Use your own API key** → provider **OpenAI Compatible** (or the built-in **Z AI** provider if your Cline build lists it).

Typical OpenAI-compatible settings:

| Field | Value |
| --- | --- |
| Base URL | `https://api.z.ai/api/coding/paas/v4` |
| API key | your z.ai key |
| Model | custom, e.g. `glm-4.6` or `glm-5.2` (use the code shown in the z.ai dashboard) |
| Images | off unless the model supports them |
| Context window | match the model card (often 128k–1M) |

If Cline offers **Z AI** as a named provider, pick that and paste the same key. Wrong base URL is the usual reason the GLM coding-plan quota does not apply.

GLM in Cline works best with **short, explicit, mechanical** instructions. That is why `AGENTS.md` is lean and command-first.

## Generate an app

From `~/Projects`, not from inside the template:

```bash
cd ~/Projects
uvx cookiecutter ./cookiecutter-agentic-python
cd <project-slug>
uv sync
uv run pytest
code .
```

Open Cline in that window. It reads `AGENTS.md` (native) and `.clinerules/`.

## What Cline reads

| File | When |
| --- | --- |
| `AGENTS.md` | Every session. Keep under ~150 lines. |
| `.clinerules/00-zai-glm.md` | Cline + z.ai / GLM provider and prompt shape. |
| `.clinerules/*.md` | Other Cline extras (workflow, Python, maintainability). |
| `.agents/docs/*` | Only when the task needs them. |
| `docs/adr/` | Structural decisions that must outlive a chat. |

Do not duplicate the same rule in three files. `AGENTS.md` is the source of truth; `.clinerules` adds Cline-only workflow.

## Daily loop (Cline + z.ai)

1. **One job per chat.** New feature or bug → new Cline conversation.
2. **Plan mode** if more than one file will change. Approve the file list before Act.
3. **@ files.** `AGENTS.md`, the module, a sample input if you have one.
4. **State the contract.** What must happen, what must not change, the exact verify command.
5. **Smallest diff.** Reject drive-by refactors.
6. **Run the command.** `uv run pytest …` / `uv run ruff check .` Done means the output is in the session, not that GLM said it passed.
7. **After two misses**, add one line to `.clinerules/` or a failing test. Not an essay.

### Prompt shape GLM follows

```
Task: add a function that normalises employee IDs to 8-digit zero-padded strings.
Put the rule in domain/. The adapter only reads the column.
Do not invent field names. If a name is missing, stop and ask.
Add pytest in tests/domain for blank and already-padded IDs.
Run: uv run pytest tests/domain -q
```

Avoid long preambles. GLM-on-Cline was tuned for concise tool use: explore → summarise → implement.

## Layout (maintainable code)

```
src/<package>/
  domain/      # rules and types — no I/O
  services/    # use cases
  adapters/    # files, HTTP, Excel, stdout
tests/         # mirrors src
```

Import direction: adapters and services may import domain. Domain imports neither.

A 40-line script can be one service plus a thin adapter. Add domain types when dicts become stringly typed or a rule is reused.

## Quality gates

```bash
uv run pytest
uv run ruff check --fix .
uv run ruff format .
uv run ty check
bash scripts/check.sh
```

Markdown is context. Anything that must always be true belongs in a test, Ruff, or CI.

## Growing rules

Add a rule only after a real miss (you corrected the agent, or the same error happened twice).

| Kind of rule | Where |
| --- | --- |
| Every session (commands, hard no's) | `AGENTS.md` |
| Cline / current sprint | `.clinerules/` |
| Long explanation | `.agents/docs/` + one-line pointer |
| Must be 100% true | test or CI |

Do not add “write clean code”, anything obvious from three files, or a second copy of an existing rule. If `AGENTS.md` passes ~150 lines, move a section into `.agents/docs/`.

Project-specific notes (Lucca fields, date formats, “never invent endpoints”) go in `.clinerules/04-<domain>.md` on that generated app — not necessarily in this generic template.

## Do not

- Work inside the template folder as if it were the app.
- Commit `.env` or raw data dumps.
- Let Cline invent APIs, columns, or test results.
- Redesign in the same chat as a one-line fix.
- Add a framework or dependency without asking.
- Maintain a 400-line `AGENTS.md`.

## First task in a new app

Paste into Cline **Plan** mode:

```
Read AGENTS.md and .agents/docs/architecture.md.
Replace the example greet() pipeline with <your first use case>.
Keep domain / services / adapters.
Delete greet only after tests exist for the new behaviour.
Do not add top-level folders. Ask if a name is ambiguous.
```
