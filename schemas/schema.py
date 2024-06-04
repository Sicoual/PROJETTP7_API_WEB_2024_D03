from flask_marshmallow import Marshmallow
from models.article import Article
from models.client import Client
from models.commande import Commande
from models.utilisateur import Utilisateur

ma = Marshmallow()

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client()

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article()

class CommandeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commande()

class UtilisateurSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Utilisateur()
