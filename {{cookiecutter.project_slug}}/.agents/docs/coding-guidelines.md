# Coding guidelines

## Naming

- Modules: `snake_case.py`, noun or verb phrase (`normalize.py`, `employee_id.py`).
- Classes: `PascalCase`, usually nouns (`ImportReport`).
- Functions: verbs (`parse_row`, `build_report`).
- Booleans: `is_`, `has_`, `should_`.

## Errors

Raise `{{ cookiecutter.package_name }}.domain.errors` exceptions for expected domain failures. Let unexpected errors bubble. Do not swallow and return `None` unless that is the documented contract.

## Data

- Prefer immutable dataclasses / frozen models for domain values.
- Parse at the edge (adapter). Domain sees clean types.
- Dates: `datetime.date` / `datetime.datetime` with timezone awareness at the boundary. Do not pass date strings through domain code.

## Dependencies

New libraries need a reason: "stdlib cannot do X cleanly." Record the choice in `docs/adr/` if it shapes the project.

## What not to do

- Utility dumping-ground modules named `helpers.py` or `utils.py` with unrelated functions.
- Circular imports. If A and B need each other, the shared bit belongs in `domain`.
- Commented-out code. Git keeps history.
