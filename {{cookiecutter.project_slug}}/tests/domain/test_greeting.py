import pytest

from {{ cookiecutter.package_name }}.domain.errors import ValidationError
from {{ cookiecutter.package_name }}.domain.greeting import greet


def test_greet_strips_whitespace() -> None:
    assert greet("  Ada  ") == "Hello, Ada."


def test_greet_rejects_blank_name() -> None:
    with pytest.raises(ValidationError, match="empty"):
        greet("   ")
