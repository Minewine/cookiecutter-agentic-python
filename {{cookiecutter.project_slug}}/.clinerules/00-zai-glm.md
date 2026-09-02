# Cline + z.ai / GLM

Use this profile when the model is GLM via z.ai.

## Provider

- Provider: Z AI, or OpenAI Compatible
- Base URL (coding plan): `https://api.z.ai/api/coding/paas/v4`
- Model: the exact code from the z.ai dashboard (e.g. `glm-4.6`, `glm-5.2`)
- Images: off unless the model card says otherwise

Wrong base URL is why coding-plan quota does not apply.

## How to talk to GLM

- Short sentences. Exact paths. Exact commands.
- Explore → state the plan in 5 lines → implement. Do not narrate.
- Never invent columns, endpoints, config keys, or test results.
- Never say tests or lint passed unless this session ran the command.
- If a name is missing from the repo, stop and ask.

## Default commands

```bash
uv run pytest
uv run pytest tests/path/test_file.py -k name -q
uv run ruff check --fix .
```
