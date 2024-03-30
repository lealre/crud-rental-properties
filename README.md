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


As showed in image below, the frontend was created using streamlit, and its where the user can perform the CRUD opeartions.

In each one of the operations the frontend sends a request to the API, created uding FastAPI. The API will be responsible to comunicate with the backend and send a response back to the frontend, displaying the result of the CRUD operation. In the first layer, Pydantic was used to validate all the inputs, by garanteeing that the schema the user is trying to send matchs with the database table schema. In case it doens match, the error message is displayed to the user.

Once the Pydantic validation is done, the SQLAlchemy was used to communicate with the PostgreSQL and perform one of the CRUD operations in Database. 

![](media/diag.png)



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
