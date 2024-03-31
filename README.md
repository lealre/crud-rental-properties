# Rental Properties CRUD Catalog with SQLAlchemy, FastAPI, Streamlit and AWS Deploy

This project consists of a web application for interacting with a catalog of rental properties stored in a PostgreSQL database hosted on Render Cloud. Users can perform all CRUD operations, which include: 

- Create a new item in the Database. 
- Accessing all items in the catalog or a specific one by passing the correesponding ID. 
- Updating a specific item in catalog by passing the corresponding ID. 
- Delete a specific item in catalog by passing the corresponding ID.

Below is a demonstration of the project deployed on EC2 AWS Cloud. The console on the right shows the API methods and their responses.

<img src="media/demo.gif" width = 1000 />

The project was built in a way where three services communicate with each other separately: database, backend, and frontend. Docker Compose was used to orchestrate the containers, allowing the frontend to communicate with the backend through the API once each one is running in independent containers.

Due to cost considerations, the EC2 instance was terminated, and the project is no longer available online, although you can run it locally by following the steps in [how to run this project](##How-to-run-this-project-locally-with-Docker).

## How it Works

The table below shows the 5 catalog fields used in the application. For House Type identification, the convention commonly used in Europe was employed, where T0 represents a house with no bedrooms, T1 represents a house with one bedroom, and so on.

| Column Name           | Python Type Hint |
|-----------------------|------------------|
| Description  | str              |
| House Type            | str (List)        |
| Price (€)            | float            |
| Area (m²)              | float            |
| Location              | str              |


As shown in the image below, the frontend was created using Streamlit, where users can perform CRUD operations.

In each of these operations, the frontend sends a request to the API created using FastAPI. The API is responsible for communicating with the backend and sending a response back to the frontend to display the result of the CRUD operation. In the first layer, Pydantic is used to validate all the inputs, ensuring that the schema the user is trying to send matches the database table schema. If it doesn't match, an error message is displayed to the user.

After Pydantic validation is completed, SQLAlchemy is used to communicate with PostgreSQL and perform one of the CRUD operations in the database

![](media/diag.png)


#### Project Folder Structure
```
├── README.md
├── backend
│   ├── Dockerfile
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── router.py
│   └── schemas.py
├── docker-compose.yaml
├── frontend
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── media
│   ├── demo.gif
│   └── diag.png
├── poetry.lock
├── pyproject.toml
└── sql
    └── create_table.sql
```

## How to run this project locally with Docker

As mentioned before, this project was built in a way that the frontend and backend run in different Docker containers. To run it locally, I used Docker CLI in a `bash` terminal.

Before proceeding, you need to create the table used by running the following SQL command in your PostgreSQL database:

```SQL
CREATE TABLE rental_properties (
    id SERIAL PRIMARY KEY,
    description VARCHAR,
    house_type VARCHAR,
    price FLOAT,
    area FLOAT,
    location VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

After accessing the folder you want to run this in your terminal, follow the steps below.

1 - Clone the repository locally:
```bash
git clone https://github.com/lealre/crud-rental-properties.git
```

2 - Access the project folder:
```bash
cd crud-rental-properties
```

3 - Create the `.env` file in the root folder, passing the respective keys from your own PostgresSQL Database. It is needed to connect the app to your database:
```bash
echo "POSTGRES_USER=<your-database-keys>" >> .env
echo "POSTGRES_PASSWORD=<your-database-keys>" >> .env
echo "POSTGRES_HOST=<your-database-keys>" >> .env
echo "POSTGRES_PORT=<your-database-keys>" >> .env
echo "POSTGRES_DB=<your-database-keys>" >> .env
```

4 - Build the Docker image
```bash
docker compose build
```

5 - Run the Docker container
```bash
docker compose up
```

6 - Access your localhost in port 8501

http://localhost:8501/

After these steps you should be able to access the app and perform all CRUD operations in your database.

Note: Make sure `.env` file is included in `.gitignore`.

