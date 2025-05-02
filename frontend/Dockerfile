FROM python:3.12-slim

ENV ROOT_FOLDER=/rental-crud

ENV POETRY_VIRTUALENVS_CREATE=false \
PYTHONPATH=${ROOT_FOLDER}

WORKDIR ${ROOT_FOLDER}

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --only frontend --no-root --no-interaction --no-ansi

COPY frontend/ frontend/

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "frontend/app.py", "--server.address=0.0.0.0"]