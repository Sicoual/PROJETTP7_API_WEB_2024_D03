from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from models.article import Article
from schemas.article_schema import ArticleSchema
from globals import api

# Définition du modèle Article pour la documentation de l'API
model_data = {
    "CodeArticle": fields.Integer(description="ID de l'article"),
    "Designation": fields.String(description="Libellé de l'article", example="Stylo"),
    "Poids": fields.String(description="Poids unitaire de l'article en kg", example="0.02"),
    "NbreDePoints": fields.String(description="Nombre de points auquel équivaut l'article", example="10"),
}

article_model = api.model("Article", model_data)
article_payload = api.model("Article", {k: v for k, v in model_data.copy().items()})

"""
Ressource Flask-RESTx pour gérer un article individuel.

Méthodes :
    get(article_id) : Récupère un article par son ID.
    put(article_id) : Met à jour un article existant.
    patch(article_id) : Met à jour partiellement un article existant.
    delete(article_id) : Désactive un article.
"""
@api.doc(params={"article_id": "ID de l'article concerné"}, model=article_model)
class ArticleResource(Resource):
    article_schema = ArticleSchema()

    def get(self, article_id):
        """
        Récupère un article par son ID.

        Paramètres :
            article_id (int) : ID de l'article à récupérer.

        Retour :
            dict : Données de l'article.
        """
        article = Article.query.get_or_404(article_id)
        return self.article_schema.dump(article)

    @api.expect(article_model)
    def put(self, article_id):
        """
        Met à jour un article existant.

        Paramètres :
            article_id (int) : ID de l'article à mettre à jour.

        Retour :
            dict : Données de l'article mis à jour.
        """
        try:
            new_article_data = self.article_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        article = Article.query.get_or_404(article_id)

        for key, value in new_article_data.items():
            if value is not None:
                setattr(article, key, value)

        db.session.commit()
        return self.article_schema.dump(article)

    def patch(self, article_id):
        """
        Met à jour partiellement un article existant.

        Paramètres :
            article_id (int) : ID de l'article à mettre à jour partiellement.

        Retour :
            dict : Données de l'article mis à jour partiellement.
        """
        try:
            new_article_data = self.article_schema.load(request.json, partial=True)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        article = Article.query.get_or_404(article_id)

        for key, value in new_article_data.items():
            if value is not None:
                setattr(article, key, value)

        db.session.commit()
        return self.article_schema.dump(article)

    def delete(self, article_id):
        """
        Désactive un article en mettant son statut à False.

        Paramètres :
            article_id (int) : ID de l'article à désactiver.

        Retour :
            dict : Données de l'article désactivé.
        """
        article = Article.query.get_or_404(article_id)
        article.Statut = False
        db.session.commit()
        return self.article_schema.dump(article)

"""
Ressource Flask-RESTx pour gérer la collection d'articles.

Méthodes :
    get() : Récupère tous les articles.
    post() : Crée un nouvel article.
"""
@api.doc(model=article_model)
class ArticleListResource(Resource):
    article_schema = ArticleSchema()

    @api.marshal_with(fields=article_model, as_list=True)
    def get(self):
        """
        Récupère tous les articles.

        Retour :
            list : Liste des articles.
        """
        all_articles = Article.query.all()
        return self.article_schema.dump(all_articles, many=True)

    def post(self):
        """
        Crée un nouvel article.

        Retour :
            dict : Données du nouvel article créé.
        """
        try:
            new_articles_data = self.article_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        new_articles = Article(
            Designation=new_articles_data["Designation"],
            Poids=new_articles_data["Poids"],
            NbreDePoints=new_articles_data["NbreDePoints"],
        )

        db.session.add(new_articles)
        db.session.commit()
        return self.article_schema.dump(new_articles)
