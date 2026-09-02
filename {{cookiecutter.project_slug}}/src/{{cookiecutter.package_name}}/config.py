"""Application settings. The only module that should read environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    log_level: str = "INFO"


def load_settings() -> Settings:
    return Settings(log_level=os.environ.get("LOG_LEVEL", "INFO"))
