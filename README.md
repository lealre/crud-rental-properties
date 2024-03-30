# Rental Properties CRUD Catalog with SQLAlchemy, FastAPI, Streamlit and AWS Deploy

This project consists of a web application to interact with a catalog of rental properties stored in a PostgreSQL database. Users can perform all CRUD operations, which include: 
- Create a new item in Database. 
- Accessing all items in the catalog or a specific one by passing the correesponding ID. 
- Updating a specific item in catalog by passing the corresponding ID. 
- Delete a specific item in catalog by passing the corresponding ID.


## How it Works

The catalog has 5 fields:

| Column Name           | Python Type Hint |
|-----------------------|------------------|
| Description  | str              |
| House Type            | List[str]        |
| Price (€)            | float            |
| Area (m2)              | float            |
| Location              | str              |


As shown in the image below, the frontend was created using Streamlit, where users can perform CRUD operations.

In each of these operations, the frontend sends a request to the API created using FastAPI. The API is responsible for communicating with the backend and sending a response back to the frontend to display the result of the CRUD operation. In the first layer, Pydantic is used to validate all the inputs, ensuring that the schema the user is trying to send matches the database table schema. If it doesn't match, an error message is displayed to the user.

After Pydantic validation is completed, SQLAlchemy is used to communicate with PostgreSQL and perform one of the CRUD operations in the database

![](media/diag.png)
<!-- ![](media/demo.gif) -->

<!-- <img src="media/demo.gif"  /> -->



### Project Folder Structure
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
├── pics
│   └── diag.png
├── poetry.lock
└── pyproject.toml
```

## How to run this project
