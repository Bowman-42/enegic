"""Custom types for enegic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import EnegicApiClient
    from .coordinator import EnegicDataUpdateCoordinator


type EnegicConfigEntry = ConfigEntry[EnegicData]


@dataclass
class EnegicData:
    """Data for the Enegic integration."""

    client: EnegicApiClient
    coordinator: EnegicDataUpdateCoordinator
    integration: Integration
