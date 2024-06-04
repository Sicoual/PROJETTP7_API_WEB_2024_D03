from schemas.schema import ma
from models.utilisateur import Utilisateur


class UtilisateurSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Utilisateur()
