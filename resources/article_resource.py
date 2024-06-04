from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from models import article
from models.article import Article,db
from schemas.article_schema import ArticleSchema

    
class ArticleResource(Resource):

    article_schema = ArticleSchema()
    article_list_schema = ArticleSchema(many=True) # Retourne plusieurs schemas
    article_patch_schema=ArticleSchema(partial=True) #Patch permet de modifier un seul attribut au minimum sans redeclarer le reste

    #Get
    def get(self, article_id=None):
        if article_id:
            article = Article.query.get_or_404(article_id)
            return self.article_schema.dump(article)
        else:
            all_articles = Article.query.all()
            return self.article_list_schema.dump(all_articles)

  # POST
    def post(self):
        try:
            new_articles_data=self.article_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400
        
        new_articles=Article(

            Designation=new_articles_data["Designation"], 
            Poids=new_articles_data["Poids"], 
            NbreDePoints=new_articles_data["NbreDePoints"], 
        )
        
        db.session.add(new_articles)
        db.session.commit()
        return self.article_schema.dump(new_articles)
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
            new_article_data = self.article_patch_schema.load(request.json)
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

