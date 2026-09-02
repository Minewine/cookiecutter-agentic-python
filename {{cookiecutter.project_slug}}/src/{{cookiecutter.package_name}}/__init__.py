"""{{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.domain.errors import DomainError
from {{ cookiecutter.package_name }}.domain.greeting import greet

__all__ = ["DomainError", "greet"]
__version__ = "0.1.0"
