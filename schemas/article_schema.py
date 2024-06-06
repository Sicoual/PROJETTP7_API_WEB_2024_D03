from globals import ma
from models.article import Article

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    """
    Schéma de sérialisation pour le modèle Article.

    Ce schéma utilise SQLAlchemyAutoSchema de Marshmallow pour 
    automatiquement générer les champs de sérialisation basés sur le modèle Article.

    Attributs :
        Meta :
            model (Article) : Modèle SQLAlchemy associé à ce schéma.
            exclude (tuple) : Champs à exclure de la sérialisation (ici, "Statut").
    """
    class Meta:
        model = Article()
        #exclude = ("Statut",)
