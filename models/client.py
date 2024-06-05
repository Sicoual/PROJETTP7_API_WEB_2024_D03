from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
)
from database import db

class Client(db.Model):
    """
    Classe représentant la table 'client' dans la base de données.

    Attributs :
        CodeCli (int) : Identifiant unique du client.
        Nom (str) : Nom de famille du client (40 caractères maximum, indexé).
        Prenom (str) : Prénom du client (30 caractères maximum).
        Adresse (str) : Adresse principale du client (50 caractères maximum).
        IdCodePostal (int) : Code postal de l'adresse du client.
        Genre (str) : Genre du client (8 caractères maximum).
        Email (str) : Adresse mail du client (255 caractères maximum).
        Statut (bool) : Statut du client, actif ou inactif (par défaut True, actif).

    Cette classe utilise SQLAlchemy pour mapper la table 'client' de la base de données.
    """
    __tablename__ = "client"

    CodeCli = Column(Integer, primary_key=True)
    Nom = Column(String(40), default=None, index=True)
    Prenom = Column(String(30), default=None)
    Adresse = Column(String(50), default=None)
    IdCodePostal = Column(Integer, default=None)
    Genre = Column(String(8), default=None)
    Email = Column(String(255), default=None)
    Statut = Column(Boolean, default=True)
