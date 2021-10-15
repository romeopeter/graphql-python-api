from flask import Flask
from flas_cors import CORS

server = Flask(__name__)

# Allows Cross-Orgin Resorce Sharing (CORS)
CORS(server)

# Views
# import app.views
