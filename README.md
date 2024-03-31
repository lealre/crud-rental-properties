# Rental Properties CRUD Catalog with SQLAlchemy, FastAPI, Streamlit and AWS Deploy

This project consists of a web application for interacting with a catalog of rental properties stored in a PostgreSQL database hosted on Render Cloud. Users can perform all CRUD operations, which include: 

- Create a new item in the Database. 
- Accessing all items in the catalog or a specific one by passing the correesponding ID. 
- Updating a specific item in catalog by passing the corresponding ID. 
- Delete a specific item in catalog by passing the corresponding ID.

Below is a demonstration of the project deployed on EC2 AWS Cloud. The console on the right shows the API methods and their responses.

<img src="media/demo.gif" width = 1000 />

## How it Works

The catalog has 5 fields:

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
└── pyproject.toml
```

## How to run this project
