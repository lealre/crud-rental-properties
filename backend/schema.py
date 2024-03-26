from pydantic import BaseModel, PositiveFloat
import datetime
from typing import Optional

class HouseBase(BaseModel):
    description: str
    house_type: str
    price: PositiveFloat
    area: PositiveFloat
    location: str

class HouseCreate(HouseBase):
    pass

class HouseResponse(HouseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class HouseUpdate(BaseModel):
    description: Optional[str] = None
    house_type: Optional[str] = None
    price: Optional[PositiveFloat] = None
    area: Optional[PositiveFloat] = None
    location: Optional[str] = None
    




