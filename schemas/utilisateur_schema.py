from globals import ma
from models.utilisateur import Utilisateur

class UtilisateurSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Utilisateur()
        exclude = ("Statut",)
