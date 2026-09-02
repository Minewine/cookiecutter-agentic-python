"""Domain exceptions. Adapters may wrap these; domain must not catch adapter errors."""


class DomainError(Exception):
    """Base class for expected, caller-facing domain failures."""


class ValidationError(DomainError):
    """Input that the domain refuses to accept."""
