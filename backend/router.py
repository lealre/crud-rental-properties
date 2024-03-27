from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, get_db
from .schemas import RentalPropertyCreate, RentalPropertyResponse, RentalPropertyUpdate
from typing import List
from .crud import get_all_properties, get_property_by_id, create_rental_property, update_property, delete_property

