from {{ cookiecutter.package_name }}.services.run_greeting import run_greeting


def test_run_greeting_writes_and_returns(captured_lines: list[str]) -> None:
    def write(message: str) -> None:
        captured_lines.append(message)

    result = run_greeting("Ada", write)

    assert result == "Hello, Ada."
    assert captured_lines == ["Hello, Ada."]
