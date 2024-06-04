from schemas.schema import ma
from models.commande import Commande

class CommandeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commande()
