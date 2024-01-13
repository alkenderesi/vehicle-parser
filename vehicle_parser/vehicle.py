"""Vehicle module."""

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
