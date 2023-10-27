from pydantic import BaseModel, ConfigDict
from pydantic.types import Decimal

class State(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    serial_number: str
    order_id: int | None = None
    state: str
    latitude: Decimal
    longitude: Decimal