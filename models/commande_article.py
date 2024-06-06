from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    ForeignKey,
    Numeric,
    Float,
)
from database import db

class CommandeArticle(db.Model):
    """
    Classe représentant la table 'commande_article' dans la base de données.

    Attributs :
        NumCde (int) : Identifiant de la commande, clé étrangère vers la table 'commande'.
        CodeArticle (int) : Identifiant de l'article, clé étrangère vers la table 'article'.
        CodeEmballage (int) : Code de l'emballage associé à l'article dans la commande.
        CodeModele (int) : Code du modèle de l'article.
        Poids (decimal) : Poids de l'article (par défaut 0.0000).
        MontantAffranchissement (float) : Montant de l'affranchissement pour l'article (par défaut 0.0000).
        Statut (bool) : Statut de l'article dans la commande, actif ou inactif (par défaut True, actif).

    Cette classe utilise SQLAlchemy pour mapper la table 'commande_article' de la base de données.
    """
    __tablename__ = "commande_article"

    NumCde = Column(Integer, ForeignKey("commande.NumCde"), primary_key=True)
    CodeArticle = Column(Integer, ForeignKey("article.CodeArticle"), primary_key=True)
    CodeEmballage = Column(Integer)
    CodeModele = Column(Integer)
    Poids = Column(Numeric, default=0.0000)
    MontantAffranchissement = Column(Float, default=0.0000)
    Statut = Column(Boolean, default=True)
