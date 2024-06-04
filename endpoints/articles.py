from flask import jsonify
from models import Article

def get_articles():
    articles = Article.query.all()
    articles_list = [
        {
            "CodeArticle": article.CodeArticle,
            "Designation": article.Designation,
            "Poids": str(article.Poids),
            "NbreDePoints": article.NbreDePoints
        }
        for article in articles
    ]
    return jsonify(articles_list)
