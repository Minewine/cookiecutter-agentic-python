# How to extend agent rules

`AGENTS.md` is loaded every session. Keep it under ~150 lines.

## Where to put a new rule

| Kind of rule | Where |
| --- | --- |
| Applies to almost every task (commands, layout, hard no's) | `AGENTS.md` |
| Cline workflow / current sprint | `.clinerules/*.md` |
| Long explanation | `.agents/docs/` and a one-line pointer in `AGENTS.md` |
| Must always be true | A test, Ruff rule, or CI step — not only markdown |

## When to add a rule

Add one after:

- the user had to correct the agent
- two sessions made the same mistake
- a change touched files you would not have guessed

Do not add:

- generic "write clean code"
- anything already obvious from reading three files
- a second copy of a rule that already lives here

When the root file grows, move a section into `.agents/docs/` and leave a pointer.
