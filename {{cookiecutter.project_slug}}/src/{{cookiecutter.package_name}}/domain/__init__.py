"""Pure domain types and rules. No I/O."""

from {{ cookiecutter.package_name }}.domain.errors import DomainError, ValidationError
from {{ cookiecutter.package_name }}.domain.greeting import greet

__all__ = ["DomainError", "ValidationError", "greet"]
