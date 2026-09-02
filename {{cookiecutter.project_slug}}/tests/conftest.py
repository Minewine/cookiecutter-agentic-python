"""Shared fixtures. Keep this file small."""

from __future__ import annotations

import pytest


@pytest.fixture
def captured_lines() -> list[str]:
    return []
