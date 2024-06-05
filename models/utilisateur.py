from sqlalchemy import (
	Boolean,
	Column,
	Integer,
	String,
	Date,
)
from database import db

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Date,
)
from database import db

class Utilisateur(db.Model):
    """
    Classe représentant la table 'utilisateur' dans la base de données.

    Attributs :
        code_utilisateur (int) : Identifiant unique de l'utilisateur.
        nom_utilisateur (str) : Nom de famille de l'utilisateur (50 caractères maximum).
        prenom_utilisateur (str) : Prénom de l'utilisateur (50 caractères maximum).
        username (str) : Pseudonyme de l'utilisateur (50 caractères maximum).
        couleur_fond_utilisateur (int) : Code couleur pour le fond de l'utilisateur (valeur entière, par défaut 0).
        date_insc_utilisateur (date) : Date d'inscription de l'utilisateur.
        Statut (bool) : Statut de l'utilisateur, actif ou inactif (par défaut True, actif).

    Cette classe utilise SQLAlchemy pour mapper la table 'utilisateur' de la base de données.
    """
    __tablename__ = "utilisateur"

    code_utilisateur = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(50), default=None)
    prenom_utilisateur = Column(String(50), default=None)
    username = Column(String(50), default=None)
    couleur_fond_utilisateur = Column(Integer, default=0)
    date_insc_utilisateur = Column(Date)
    Statut = Column(Boolean, default=True)
