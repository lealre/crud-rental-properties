from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import RentalPropertyCreate, RentalPropertyResponse, RentalPropertyUpdate
from typing import List
from .crud import get_all_properties, get_property_by_id, create_rental_property, update_property, delete_property

router = APIRouter()

@router.get("/properties/", response_model= List[RentalPropertyResponse])
def read_all_items(db: Session = Depends(get_db)):
    properties_db = get_all_properties(db)
    return properties_db

@router.get("/properties/{property_id}", response_model= RentalPropertyResponse)
def read_item_by_id(property_id: int, db: Session = Depends(get_db)):
    property_db = get_property_by_id(db, property_id= property_id)
    if property_db is None:
        raise HTTPException(status_code = 404, detail= "There is no property with this id.")
    return property_db

@router.post("/properties/", response_model= RentalPropertyResponse)
def create_item(property: RentalPropertyCreate, db: Session = Depends(get_db)):
    return create_rental_property(db=db, rental_property = property)

@router.delete("/properties/{property_id}", response_model = RentalPropertyResponse)
def delete_item(property_id: int, db: Session = Depends(get_db)):    
    property_db =  delete_property(db=db, property_id= property_id)
    if property_db is None:
        raise HTTPException(status_code = 404, detail= "There is no property with this id to delete.")
    return property_db

@router.put("/properties/{property_id}", response_model= RentalPropertyResponse)
def update_item(property_id: int, property: RentalPropertyUpdate, db: Session = Depends(get_db)):
    property_db =  update_property(db=db, property_id= property_id, property= property)
    if property_db is None:
        raise HTTPException(status_code = 404, detail= "There is no property with this id to update.")
    return property_db