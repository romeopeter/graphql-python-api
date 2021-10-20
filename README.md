# A Python-GraphQL API implementation

The project uses Python's Ariadne library to integrate GraphQL.

## Main project structure

The following are contained in the _app_ package directory.
 - `__init__.py`: Initialization file for the Flask object.

 - `models.py`: Database model

 - `views.py`: GraphQL binding and server routes 

**API**

API uses GraphQL for CRUD functionalities.

 - `schema.graphql`: GraphQL schema to validate data from client and resolvers
 - `api_resolvers.py`: Logic to resolve all client requests

## How to reproduce.

Active [virtual environment](https://docs.python.org/3/library/venv.html) for Python.

Run `pip install -e .` to install required package from _setup.py_ file.

Create _.flaskenv_ environment file and add the following: `FLASK_APP=app` and `FLASK_ENV=development`.

To start server, run `flask run` in the terminal.