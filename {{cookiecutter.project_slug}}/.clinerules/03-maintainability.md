# Maintainability

Write code a future agent (and a tired human) can change safely.

- One module, one reason to change.
- Names describe the business idea (`normalize_employee_id`), not the mechanism (`process_data2`).
- Public functions get a one-line docstring only when the name is not enough.
- Keep functions short enough to test without mocks stacked five deep.
- If a function needs more than two collaborators, it is probably a service — put it in `services/`.
- Duplication of *knowledge* (the same rule in two places) is worse than duplication of *lines*. Extract the rule.
- Do not add an abstraction for a single call site.
- Configuration is data. Do not scatter magic strings; put them in `config.py` or a typed settings object.
- When you change behaviour, add or update a test that would have failed before the change.
