"""Vehicle module."""

import os
import json
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Vehicle:
    """Base class for vehicles."""

    id: str
    brand: str


@dataclass(frozen=True)
class Car(Vehicle):
    """Car class representing a car."""

    doors: int


@dataclass(frozen=True)
class Bicycle(Vehicle):
    """Bicycle class representing a bicycle."""

    max_weight: float


class VehicleHandler:
    """Vehicle handler class for loading vehicles from json files."""

    def load(path: str) -> Vehicle:
        """
        Load a vehicle from a json file.

        Args:
            * path (`str`): Path to the json file.

        Returns:
            `Vehicle`: The vehicle instance.
        """

        with open(path, "r") as file:
            data: dict = json.load(file)

        data["id"] = os.path.splitext(os.path.basename(path))[0]
        vehicle_type = data.pop("type")

        if vehicle_type == "car":
            return Car(**data)

        if vehicle_type == "bicycle":
            return Bicycle(**data)

        raise ValueError(f"Unknown vehicle type: {vehicle_type}")
