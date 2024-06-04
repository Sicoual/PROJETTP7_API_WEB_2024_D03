from flask import Flask
from flask_restx import Api, Resource
from models.article import Article
from models.client import Client
from models.commande import Commande
from models.utilisateur import Utilisateur
from schemas.schema import ArticleSchema, ClientSchema, CommandeSchema, UtilisateurSchema
from globals import api

@api.doc(params={'id': 'An ID'})
class ClientResource(Resource):
    client_schema = ClientSchema()
    client_list_schema = ClientSchema(many=True) # Retourne plusieurs schemas

    def get(self, client_id=None):
        if client_id:
            client = Client.query.get_or_404(client_id)
            return self.client_schema.dump(client)
        else:
            all_clients = Client.query.all()
            return self.client_list_schema.dump(all_clients)

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

class UtilisateurResource(Resource):

    utilisateur_schema = UtilisateurSchema()
    utilisateur_list_schema = UtilisateurSchema(many=True) # Retourne plusieurs schemas

    def get(self, utilisateur_id=None):
        if utilisateur_id:
            utilisateur = Utilisateur.query.get_or_404(utilisateur_id)
            return self.utilisateur_schema.dump(utilisateur)
        else:
            all_utilisateurs = Utilisateur.query.all()
            return self.utilisateur_list_schema.dump(all_utilisateurs)
