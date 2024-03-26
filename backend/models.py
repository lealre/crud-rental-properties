from .database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

class RentalHouse():
    __tablename__ = "houses"

    id = Column(Integer, primary_key = True)
    description = Column(String)
    house_type = Column(String)
    price = Column(Float)
    area = Column(Float)
    location = Column(String)
    # zip_code = Column(String)
    created_at = Column(DateTime(timezone = True), default = func.now())
    
