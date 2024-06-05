from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api

# Initialisation de l'application Flask
app = Flask(__name__)

# Initialisation de l'API Flask-RESTx
api = Api(app)

# Initialisation de Marshmallow pour la sérialisation
ma = Marshmallow(app)