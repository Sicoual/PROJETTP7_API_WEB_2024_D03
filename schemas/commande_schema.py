from globals import ma
from models.commande import Commande

class CommandeSchema(ma.SQLAlchemyAutoSchema):
    """
    Schéma de sérialisation pour le modèle Commande.

    Ce schéma utilise SQLAlchemyAutoSchema de Marshmallow pour 
    automatiquement générer les champs de sérialisation basés sur le modèle Commande.

    Attributs :
        Meta :
            model (Commande) : Modèle SQLAlchemy associé à ce schéma.
            include_fk (bool) : Inclure les clés étrangères dans la sérialisation.
    """
    class Meta:
        model = Commande()
        include_fk = True
