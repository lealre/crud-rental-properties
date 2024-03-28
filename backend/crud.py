from sqlalchemy.orm import Session
from .schemas import RentalPropertyUpdate, RentalPropertyCreate
from .models import RentalProperty

def get_all_properties(db: Session):
    """
    Retrieve all rental properties from the database.
    """
    return db.query(RentalProperty).all()

def get_property_by_id(db: Session, property_id: int):
    """
    Retrieve a rental property by its ID.
    """
    return db.query(RentalProperty).filter(RentalProperty.id == property_id).first()

def create_rental_property(db: Session, rental_property: RentalPropertyCreate):
    """
    Create a new rental property in the database.
    """
    db_property = RentalProperty(**rental_property.model_dump())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def update_property(db: Session, property_id: int, property: RentalPropertyUpdate):
    """
    Update a rental property from the database by its ID.
    """    
    db_property = db.query(RentalProperty).filter(RentalProperty.id == property_id).first()

    if db_property is None:
        return None
    
    if property.description is not None:
        db_property.description = property.description
    if property.house_type is not None:
        db_property.house_type = property.house_type
    if property.price is not None:
        db_property.price = property.price
    if property.area is not None:
        db_property.area = property.area
    if property.location is not None:
        db_property.location = property.location

    db.commit()
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    """
    Delete a rental property from the database by its ID.
    """
    db_property = db.query(RentalProperty).filter(RentalProperty.id == property_id).first()
    if db_property:
        db.delete(db_property)
        db.commit()
    return db_property


