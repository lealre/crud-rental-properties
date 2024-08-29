from pydantic import BaseModel

from backend.model import NumBedrooms


class Message(BaseModel):
    message: str


class PropertyRequest(BaseModel):
    description: str
    number_bedrooms: NumBedrooms
    price: float
    area: float
    location: str


class PropertyResponse(PropertyRequest):
    id: int


class PropertiesList(BaseModel):
    properties: list[PropertyResponse]


class PropertyUpdateRequest(BaseModel):
    description: str | None = None
    number_bedrooms: NumBedrooms | None = None
    price: float | None = None
    area: float | None = None
    location: str | None = None
