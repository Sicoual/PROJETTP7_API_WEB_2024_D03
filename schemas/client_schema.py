from schemas.schema import ma
from models.client import Client

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Client()