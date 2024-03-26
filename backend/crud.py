from sqlalchemy.orm import Session
from .schemas import RentalPropertyUpdate, RentalPropertyCreate
from .models import RentalProperty

def get_all_houses(db: Session):
    return db.query(RentalProperty).all()

def get_by_id(db: Session, house_id: int):
    return db.query(RentalProperty).filter(RentalProperty.id == house_id).first()

# def create_rental_property_item(db: Session, rental_property: HouseCreate)


