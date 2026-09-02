# Workflow (Cline)

Use Plan mode for anything that touches more than one module or changes behaviour.

1. Explore the existing files. Do not assume names.
2. State the plan: files, behaviour, how you will verify.
3. Wait if the user asked for a plan first.
4. Implement the smallest diff.
5. Run the relevant command from `AGENTS.md`.
6. Report what changed and what you ran.

Never say tests or lint passed unless you ran them in this session.

Prefer a new conversation for a new feature. Do not drag an old context into unrelated work.

If blocked (missing credential, unknown schema, ambiguous rule), stop and ask. Do not guess production data shapes.
