FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --only frontend --no-interaction --no-ansi

COPY frontend/ frontend/

EXPOSE 8501

CMD poetry run streamlit run frontend/app.py --server.address=0.0.0.0