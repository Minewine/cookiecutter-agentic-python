# 0001. Layered src layout

- Status: accepted
- Date: 2026-09-02

## Context

Agentic sessions rewrite code quickly. Without a default place for logic vs I/O, business rules leak into scripts and become untestable.

## Decision

Use `domain` / `services` / `adapters` under `src/{{ cookiecutter.package_name }}/`. Domain has no I/O. Import direction is inward.

## Consequences

Tests for rules stay fast. A 40-line tool can still skip an unused layer. Agents have a map instead of inventing a new folder each session.
