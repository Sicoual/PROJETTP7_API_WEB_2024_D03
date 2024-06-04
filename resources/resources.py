from flask_restful import Resource
from models.article import Article
from models.client import Client
from models.commande import Commande
from models.utilisateur import Utilisateur
from schemas.schema import ArticleSchema, CommandeSchema


class ArticleResource(Resource):

    article_schema = ArticleSchema()
    article_list_schema = ArticleSchema(many=True) # Retourne plusieurs schemas

    def get(self, article_id=None):
        if article_id:
            article = Article.query.get_or_404(article_id)
            return self.article_schema.dump(article)
        else:
            all_articles = Article.query.all()
            return self.article_list_schema.dump(all_articles)

class CommandeResource(Resource):

    commande_schema = CommandeSchema()
    commande_list_schema = CommandeSchema(many=True) # Retourne plusieurs schemas

    def get(self, commande_id=None):
        if commande_id:
            commande = Commande.query.get_or_404(commande_id)
            return self.commande_schema.dump(commande)
        else:
            all_commandes = Commande.query.all()
            return self.commande_list_schema.dump(all_commandes)

