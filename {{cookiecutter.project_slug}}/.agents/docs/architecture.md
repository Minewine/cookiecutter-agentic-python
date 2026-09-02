# Architecture

Start small. This layout is a default, not a religion.

## Layers

| Layer | Allowed to do | Must not do |
| --- | --- | --- |
| `domain` | Types, validation, calculations, domain errors | Read files, call HTTP, talk to Excel/DB, log as a side effect of logic |
| `services` | Orchestrate a use case: load → domain → save | Embed CSV dialects or HTTP retry logic |
| `adapters` | Files, APIs, spreadsheets, databases, clocks | Contain business rules that should be unit-tested without I/O |

Import direction: `adapters` and `services` may import `domain`. `domain` imports nothing from the other two.

## When to skip a layer

A 40-line script with one job can live as a single module under `services/` plus a tiny adapter. Add `domain/` when a rule is reused or needs its own tests.

## Growth path

1. One use case, one service function.
2. Extract domain types when dictionaries get stringly-typed.
3. Extract adapters when the same I/O is used twice or needs fakes in tests.
4. Split packages only when a folder is painful to navigate.

## Config

`src/{{ cookiecutter.package_name }}/config.py` is the only place that reads environment variables for the app. Callers receive a settings object. Tests pass settings in directly.
