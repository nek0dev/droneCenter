from pydantic import BaseModel, ConfigDict
from pydantic.types import Decimal

class CreateDrone(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    serial_number: str
    max_weight: Decimal
    dimensions: list[int]
    product_dimensions: list[int]
    max_distance: int
    latitude: Decimal
    longitude: Decimal

class ChangeDrone(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    serial_number: str
    max_weight: Decimal
    dimensions: list[int]
    product_dimensions: list[int]
    max_distance: int
    latitude: Decimal
    longitude: Decimal

class Drone(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    serial_number: str
    max_weight: Decimal
    dimensions: list[int]
    product_dimensions: list[int]
    max_distance: int

class DeleteDrone(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    serial_number: str