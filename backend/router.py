from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import (
    add_property,
    delete_property,
    get_all_properties,
    get_property_by_id,
    update_property,
)
from backend.database import get_session
from backend.schema import (
    Message,
    PropertiesList,
    PropertyRequest,
    PropertyResponse,
    PropertyUpdateRequest,
)

router = APIRouter(prefix='/property')

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.post(
    '/', response_model=PropertyResponse, status_code=HTTPStatus.CREATED
)
async def add_property_route(
    property: PropertyRequest,
    session: SessionDep,
):
    db_property = await add_property(session=session, property=property)

    return db_property


@router.get('/{property_id}', response_model=PropertyResponse)
async def get_property_by_id_route(session: SessionDep, property_id: int):
    db_property = await get_property_by_id(
        session=session, property_id=property_id
    )

    if not db_property:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Property ID was not found.',
        )

    return db_property


@router.get('/', response_model=PropertiesList)
async def get_all_properties_route(
    session: SessionDep, skip: int = 0, limit: int = 100
):
    properties_list = await get_all_properties(
        session=session, skip=skip, limit=limit
    )

    return {'properties': properties_list}


@router.patch('/{property_id}', response_model=PropertyResponse)
async def update_property_route(
    session: SessionDep, property_id: int, property: PropertyUpdateRequest
):
    property_args = property.model_dump(exclude_unset=True)

    db_property = await update_property(
        session=session, property_id=property_id, property=property_args
    )

    if not db_property:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Property ID was not found.',
        )

    return db_property


@router.delete('/{property_id}', response_model=Message)
async def delete_property_route(session: SessionDep, property_id: int):
    db_property = await delete_property(
        session=session, property_id=property_id
    )

    if not db_property:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Property ID was not found.',
        )

    return {'message': 'Property deleted.'}
