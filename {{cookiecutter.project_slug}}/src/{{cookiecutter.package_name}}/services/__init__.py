"""Use-case orchestration. Import domain + adapters here."""

from {{ cookiecutter.package_name }}.services.run_greeting import run_greeting

__all__ = ["run_greeting"]
