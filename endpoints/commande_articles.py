from flask import jsonify
from models import CommandeArticle

def get_commande_articles():
    commande_articles = CommandeArticle.query.all()
    commande_articles_list = [
        {
            "NumCde": commande_article.NumCde,
            "CodeArticle": commande_article.CodeArticle,
            "CodeEmballage": commande_article.CodeEmballage,
            "CodeModele": commande_article.CodeModele,
            "Poids": str(commande_article.Poids),
            "MontantAffranchissement": commande_article.MontantAffranchissement
        }
        for commande_article in commande_articles
    ]
    return jsonify(commande_articles_list)
