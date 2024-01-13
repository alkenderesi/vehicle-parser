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


@dataclass
class VehicleCollection:
    """Vehicle collection class for storing vehicles."""

    vehicles: list[Vehicle] = field(default_factory=list)

    def __str__(self) -> str:
        vehicles_str = "\n".join([f" - {vehicle}" for vehicle in self.vehicles])
        return f"VehicleCollection:\n{vehicles_str}"

    def load(self, dir: str, handler: VehicleHandler) -> None:
        """
        Extend the list of vehicles by loading new ones from a directory.

        Args:
            * dir (`str`): Path to the directory.
            * handler (`VehicleHandler`): The handler to use for loading.
        """

        print(f"Checking directory: {dir}")

        for dir_content in os.listdir(dir):
            sub_path = os.path.join(dir, dir_content)

            if os.path.isdir(sub_path):
                self.load(sub_path, handler)

            elif os.path.isfile(sub_path):
                vehicle = handler.load(sub_path)
                self.vehicles.append(vehicle)
                print(f"Loaded {vehicle} from file: {sub_path}")
