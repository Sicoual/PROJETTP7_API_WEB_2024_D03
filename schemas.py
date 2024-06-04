from flask_marshmallow import Marshmallow
from models import Article, Client, Commande, Utilisateur

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
