FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --only backend --no-interaction --no-ansi

COPY backend/ backend/

EXPOSE 8000

CMD poetry run fastapi run backend/main.py --host 0.0.0.0
