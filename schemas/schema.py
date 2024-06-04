from flask_marshmallow import Marshmallow
from models.article import Article
from models.commande import Commande

ma = Marshmallow()


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article()

class CommandeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commande()

