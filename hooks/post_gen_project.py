"""Clean optional files after generation."""

from __future__ import annotations

from pathlib import Path

INCLUDE_CLI = "{{ cookiecutter.include_cli }}" == "y"
LICENSE = "{{ cookiecutter.license }}"

root = Path.cwd()

if not INCLUDE_CLI:
    cli = root / "src" / "{{ cookiecutter.package_name }}" / "cli.py"
    if cli.exists():
        cli.unlink()
    pyproject = root / "pyproject.toml"
    text = pyproject.read_text()
    start = text.find("[project.scripts]")
    if start != -1:
        end = text.find("[", start + 1)
        if end == -1:
            end = len(text)
        text = text[:start] + text[end:]
        pyproject.write_text(text)


if LICENSE == "None":
    license_file = root / "LICENSE"
    if license_file.exists():
        license_file.unlink()

print()
print("Project generated.")
print()
print("Next:")
print("  cd {{ cookiecutter.project_slug }}")
print("  uv sync")
print("  uv run pytest")
print("  # Open in VS Code and start Cline")
print()
