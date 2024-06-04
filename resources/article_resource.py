from flask import request
from flask_restx import Resource
from marshmallow import ValidationError
from models.article import Article,db
from schemas.article_schema import ArticleSchema

class ArticleResource(Resource):
    article_schema = ArticleSchema()

    #Get
    def get(self, article_id):
        article = Article.query.get_or_404(article_id)
        return self.article_schema.dump(article)

    # PUT
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


class ArticleListResource(Resource):
    article_schema = ArticleSchema()

    #Get
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
