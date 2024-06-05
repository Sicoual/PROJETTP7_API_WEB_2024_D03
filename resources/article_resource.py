from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from models.article import Article
from schemas.article_schema import ArticleSchema
from globals import api

model_data = {
    "CodeArticle": fields.Integer(description="ID de l'article", example=1),
    "Designation": fields.String(description="Libellé de l'article", example="Stylo"),
    "Poids": fields.String(description="Poids unitaire de l'article en kg", example="0.02"),
    "NbreDePoints": fields.String(description="Nombre de points auquel équivaut l'article", example="10"),
}

article_model = api.model("Article", model_data)
article_payload = api.model("Article Payload", {k: v for k, v in model_data.items() if k not in ["CodeArticle"]})

@api.doc(params={"article_id": "ID de l'article concerné"}, model=article_model)
class ArticleResource(Resource):
    article_schema = ArticleSchema()

    # Get
    @api.doc(description="Récupérer un article par son ID",
             responses={404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID de l'article n'a pas été renseigné"})
    def get(self, article_id):
        article = Article.query.get_or_404(article_id)
        return self.article_schema.dump(article)

    # PUT
    @api.expect(article_payload)
    @api.doc(description="Modifier un article existant", 
             responses={400: "Erreur de validation des données", 
             404: "L'ID renseigné n'existe pas en base de données", 
             405: "L'ID de l'article n'a pas été renseigné"})
    def put(self, article_id):
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

    # PATCH
    @api.expect(article_payload)
    @api.doc(description="Modifier les attributs d'un article existant", 
             responses={400: "Erreur de validation des données", 
                404: "L'ID renseigné n'existe pas en base de données", 
                405: "L'ID de l'article n'a pas été renseigné"})
    def patch(self, article_id):
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

    # DELETE
    @api.doc(description="Supprimer un article", 
             responses={404: "L'ID renseigné n'existe pas en base de données", 
                        405: "L'ID de l'article n'a pas été renseigné"})
    def delete(self, article_id):
        article = Article.query.get_or_404(article_id)
        article.Statut = False
        db.session.commit()
        return self.article_schema.dump(article)

@api.doc(model=article_model)
class ArticleListResource(Resource):
    article_schema = ArticleSchema()

    # Get
    @api.marshal_with(article_model, as_list=True)
    @api.doc(description="Récupérer la liste de tous les articles", 
             responses={404: "Aucun article trouvé"})
    def get(self):
        all_articles = Article.query.all()
        if not all_articles:
            return {"message": "Aucun article trouvé"}, 404
        return self.article_schema.dump(all_articles, many=True)

    # POST
    @api.expect(article_payload)
    @api.doc(description="Ajouter un nouvel article", 
             responses={400: "Erreur de validation des données"})
    def post(self):
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
