"""Validate cookiecutter inputs before files are rendered."""

from __future__ import annotations

import re
import sys

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PKG_RE = re.compile(r"^[a-z_][a-z0-9_]*$")

slug = "{{ cookiecutter.project_slug }}"
package = "{{ cookiecutter.package_name }}"

errors: list[str] = []

if not SLUG_RE.match(slug):
    errors.append(
        f"project_slug={slug!r} must be lowercase kebab-case (e.g. my-project)."
    )

if not PKG_RE.match(package) or package in {
    "test",
    "tests",
    "src",
    "lib",
    "types",
}:
    errors.append(
        f"package_name={package!r} must be a valid Python identifier "
        "(lowercase, underscores, not a reserved module name)."
    )

if errors:
    print("Cookiecutter validation failed:")
    for item in errors:
        print(f"  - {item}")
    sys.exit(1)
