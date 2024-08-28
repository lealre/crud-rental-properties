from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.model import Property
from backend.schema import PropertyRequest


async def add_property(session: AsyncSession, property: PropertyRequest):
    db_property = Property(**property.model_dump())

    async with session.begin():
        session.add(db_property)
        await session.commit()

    await session.refresh(db_property)
    return db_property


async def get_all_properties(session: AsyncSession, limit: int, skip: int):
    async with session.begin():
        properties_list = await session.scalars(
            select(Property).limit(limit).offset(skip)
        )

        return properties_list


async def get_property_by_id(session: AsyncSession, property_id: int):
    async with session.begin():
        db_property = await session.scalar(
            select(Property).where(Property.id == property_id)
        )

        if not db_property:
            return

        return db_property


async def update_property(
    session: AsyncSession, property_id: int, property: dict
):
    async with session.begin():
        db_property = await session.scalar(
            select(Property).where(Property.id == property_id)
        )

        if not db_property:
            return

        for key, value in property.items():
            setattr(db_property, key, value)

        session.add(db_property)
        await session.commit()

    await session.refresh(db_property)
    return db_property


async def delete_property(session: AsyncSession, property_id: int):
    async with session.begin():
        db_property = await session.scalar(
            select(Property).where(Property.id == property_id)
        )

        if not db_property:
            return

        await session.delete(db_property)
        await session.commit()

        return True
