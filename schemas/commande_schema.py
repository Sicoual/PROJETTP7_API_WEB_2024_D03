from globals import ma
from models.commande import Commande

class CommandeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commande()
        include_fk = True
        exclude = ("Statut",)
