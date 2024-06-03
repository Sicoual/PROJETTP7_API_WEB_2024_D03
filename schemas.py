from flask_marshmallow import Marshmallow
from models import Client

ma = Marshmallow()

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client()
