from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api

app = Flask(__name__)

api = Api(app)

ma = Marshmallow(app)
