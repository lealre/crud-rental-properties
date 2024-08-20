from pydantic import BaseModel

from app.model import NumBedrooms

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