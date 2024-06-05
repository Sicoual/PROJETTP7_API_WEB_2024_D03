from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Float,
)
from database import db

class Commande(db.Model):
    """
    Classe représentant la table 'commande' dans la base de données.

    Attributs :
        NumCde (int) : Identifiant unique de la commande.
        CodeClient (int) : Identifiant du client associé à la commande, clé étrangère vers la table 'client'.
        DateCde (date) : Date de création de la commande.
        MtTotal (float) : Montant total de la commande en EUR.
        CodeOperateur (int) : Code de l'opérateur associé à la commande.
        NSuivi (str) : Numéro de suivi de la commande (50 caractères maximum).
        DateExpedition (date) : Date d'expédition de la commande.
        Statut (bool) : Statut de la commande, actif ou inactif (par défaut True, actif).

    Cette classe utilise SQLAlchemy pour mapper la table 'commande' de la base de données.
    """
    __tablename__ = "commande"

    NumCde = Column(Integer, primary_key=True)
    CodeClient = Column(Integer, ForeignKey("client.CodeCli"))
    DateCde = Column(Date)
    MtTotal = Column(Float)
    CodeOperateur = Column(Integer)
    NSuivi = Column(String(50), default=None)
    DateExpedition = Column(Date)
    Statut = Column(Boolean, default=True)
