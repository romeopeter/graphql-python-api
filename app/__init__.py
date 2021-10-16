from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

server = Flask(__name__)
# Allows Cross-Orgin Resorce Sharing (CORS)
CORS(server)

# Loads DB env variables
config = dotenv_values(".flaskenv")


server.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{config['DB_USERNAME']}:{config['DB_PASSWORD']}@fanny.db.elephantsql.com/vgunlndd"
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)

# Views & models
import app.views

import app.models
