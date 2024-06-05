from globals import ma
from models.article import Article

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article()
        #exclude = ("Statut",)
