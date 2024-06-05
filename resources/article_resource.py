from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from models.article import Article
from schemas.article_schema import ArticleSchema
from globals import api

model_data = {
    "CodeArticle": fields.Integer(description="ID de l'article"),
    "Designation": fields.String(description="Libellé de l'article", example="Stylo"),
    "Poids": fields.String(description="Poids unitaire de l'article en kg", example="0.02"),
    "NbreDePoints": fields.String(description="Nombre de points auquel équivaut l'article", example="10"),
}

article_model = api.model("Article", model_data)
article_payload = api.model("Article", {k: v for k, v in model_data.copy().items()})

@api.doc(params={"article_id": "ID de l'article concerné"}, model=article_model)
class ArticleResource(Resource):
    article_schema = ArticleSchema()

    #Get
    def get(self, article_id):
        article = Article.query.get_or_404(article_id)
        return self.article_schema.dump(article)

    # PUT
    @api.expect(article_model)
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

    #PATCH
    #@api.expect(article_payload)
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
    def delete(self,article_id):
        article=Article.query.get_or_404(article_id)
        article.Statut=False
        db.session.commit()
        return self.article_schema.dump(article)

@api.doc(model=article_model)
class ArticleListResource(Resource):
    article_schema = ArticleSchema()

    #Get
    @api.marshal_with(fields=article_model, as_list=True)
    def get(self):
        all_articles = Article.query.all()
        return self.article_schema.dump(all_articles, many=True)

    # POST
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
