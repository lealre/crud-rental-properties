from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import create_property, get_all_properties
from app.database import get_session
from app.schema import PropertyResponse, PropertyRequest, PropertiesList

router = APIRouter(prefix='/property')

SessionDep = Annotated[AsyncSession, Depends(get_session)]

@router.post('/')
async def add_property(
    property: PropertyRequest,
    session: SessionDep, 
):


    db_property = await create_property(
        session=session, property=property
    )

    return db_property


@router.get('/', response_model=PropertiesList)
def get_all_properties(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100
):
    properties_list = get_all_properties(session=session)

    return {'properties': properties_list}