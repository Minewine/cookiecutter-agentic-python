# Python

- Python {{ cookiecutter.python_version }}. Do not use newer syntax.
- Package manager: `uv` and `pyproject.toml`. Never add `requirements.txt`. Never use raw `pip install` for project deps.
- Add a runtime dep with `uv add <pkg>`. Add a dev dep with `uv add --dev <pkg>`.
- Formatter and linter: Ruff. Type checker: `ty`.
- No `print` in library code. Use `logging.getLogger(__name__)`.
- No bare `except:`. Catch the narrowest exception that is real.
- Prefer explicit function arguments over hidden global state.
- Dataclasses or simple functions first. Do not introduce a framework without asking.
