from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schema import PropertyRequest
from app.model import Property


async def create_property(session: AsyncSession, property: PropertyRequest):
    db_property = Property(**property.model_dump())

    async with session.begin():
        session.add(db_property)
        await session.flush()
        await session.commit()
        session.refresh(db_property)
    
    return db_property


async def get_all_properties(session: AsyncSession, skip: int, limit: int):
    async with session:
        properties_list = await session.scalars(
            select(Property).offset(skip).limit(limit)
        )
        return properties_list 