from pydantic import BaseModel, PositiveFloat
from datetime import datetime
from typing import Optional

class RentalPropertyBase(BaseModel):
    description: str
    house_type: str
    price: PositiveFloat
    area: PositiveFloat
    location: str

class RentalPropertyCreate(RentalPropertyBase):
    pass

class RentalPropertyResponse(RentalPropertyBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class RentalPropertyUpdate(BaseModel):
    description: Optional[str] = None
    house_type: Optional[str] = None
    price: Optional[PositiveFloat] = None
    area: Optional[PositiveFloat] = None
    location: Optional[str] = None
    




