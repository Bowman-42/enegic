"""Custom types for integration_blueprint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import EnegicApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type EnegicConfigEntry = ConfigEntry[EnegicData]


@dataclass
class EnegicData:
    """Data for the Blueprint integration."""

    client: EnegicApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
