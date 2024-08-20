from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import Settings


engine = create_async_engine(Settings().DATABSE_URL, echo=True)

AsyncSesssionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine,
    class_=AsyncSession
)


async def get_session():
    with AsyncSesssionLocal() as session:
        yield session