from globals import ma
from models.client import Client

class ClientSchema(ma.SQLAlchemyAutoSchema):
    """
    Schéma de sérialisation pour le modèle Client.

    Ce schéma utilise SQLAlchemyAutoSchema de Marshmallow pour 
    automatiquement générer les champs de sérialisation basés sur le modèle Client.

    Attributs :
        Meta :
            model (Client) : Modèle SQLAlchemy associé à ce schéma.
    """
    class Meta:
        model = Client()
