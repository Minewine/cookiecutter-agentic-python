"""Example service: domain rule + an output port."""

from __future__ import annotations

from collections.abc import Callable

from {{ cookiecutter.package_name }}.domain.greeting import greet

Writer = Callable[[str], None]


def run_greeting(name: str, write: Writer) -> str:
    message = greet(name)
    write(message)
    return message
