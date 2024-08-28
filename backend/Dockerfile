FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /rental-crud
COPY alembic.ini pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --only backend --no-interaction --no-ansi

COPY backend/ backend/

EXPOSE 8000

ENTRYPOINT ["sh", "/rental-crud/backend/entrypoint.sh"]

