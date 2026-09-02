# Testing

## Policy

- Domain: unit tests, no I/O, no mocks if you can pass values in.
- Services: tests with fake adapters (in-memory).
- Adapters: thin tests or a marked integration test if a real resource exists.

## How to run

```bash
uv run pytest
uv run pytest tests/domain -q
uv run pytest tests/path/test_file.py -k name -vv
```

## Style

- File name: `test_<module>.py`.
- Test name: `test_<behaviour>_<condition>`.
- Arrange / act / assert. One behaviour per test.
- Parametrize repeated cases rather than copy-paste.
- Fixtures live next to the tests that need them. Shared fixtures go in `tests/conftest.py`.

## Done means

The new behaviour has a test that failed before the change (or you can explain why a test is the wrong tool — e.g. a one-line rename).
