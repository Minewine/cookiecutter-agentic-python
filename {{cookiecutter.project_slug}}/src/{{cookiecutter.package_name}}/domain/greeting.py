"""Example domain function — replace with real rules."""

from {{ cookiecutter.package_name }}.domain.errors import ValidationError


def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValidationError("name must not be empty")
    return f"Hello, {cleaned}."
