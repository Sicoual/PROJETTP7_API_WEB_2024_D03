from sqlalchemy import (
    Boolean,
    Column,
    Float,
    Integer,
    String
)
from database import db

class Article(db.Model):
    """
    Classe représentant la table 'article' dans la base de données.

    Attributs :
        CodeArticle (int) : Identifiant unique de l'article.
        Designation (str) : Libellé de l'article (50 caractères maximum).
        Poids (float) : Poids unitaire de l'article en kg (par défaut 0.0000).
        NbreDePoints (int) : Nombre de points auquel équivaut l'article (par défaut 0).
        Statut (bool) : Statut de l'article, actif ou inactif (par défaut True, actif).

    Cette classe utilise SQLAlchemy pour mapper la table 'article' de la base de données.
    """
    __tablename__ = "article"

    CodeArticle = Column(Integer, primary_key=True)
    Designation = Column(String(50), default=None)
    Poids = Column(Float(), default=0.0000)
    NbreDePoints = Column(Integer, default=0)
    Statut = Column(Boolean, default=True)
