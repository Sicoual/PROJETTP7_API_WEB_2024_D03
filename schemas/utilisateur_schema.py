from globals import ma
from models.utilisateur import Utilisateur

class UtilisateurSchema(ma.SQLAlchemyAutoSchema):
    """
    Schéma de sérialisation pour le modèle Utilisateur.

    Ce schéma utilise SQLAlchemyAutoSchema de Marshmallow pour 
    automatiquement générer les champs de sérialisation basés sur le modèle Utilisateur.

    Attributs :
        Meta :
            model (Utilisateur) : Modèle SQLAlchemy associé à ce schéma.
    """
    class Meta:
        model = Utilisateur()
