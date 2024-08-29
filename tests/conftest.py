import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from backend.database import get_session
from backend.main import app
from backend.model import table_registry


@pytest.fixture(scope='session')
async def engine():
    _engine = create_async_engine('sqlite+aiosqlite:///:memory:', future=True)

    async with _engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.create_all)

    yield _engine

    async with _engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.drop_all)

    await _engine.dispose()


@pytest.fixture
async def session(engine):
    TestingAsynSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=True,
        expire_on_commit=False,
        bind=engine,
        class_=AsyncSession,
    )

    async with TestingAsynSessionLocal() as session:
        yield session


@pytest.fixture
async def client(session):
    def get_session_override():
        yield session

    app.dependency_overrides[get_session] = get_session_override

    async with AsyncClient(app=app, base_url='http://localhost') as client:
        yield client

    app.dependency_overrides.clear()
