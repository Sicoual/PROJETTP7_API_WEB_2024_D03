from sqlalchemy import (
	Boolean,
	Column,
	Integer,
	String,
	Date,
)
from database import db


class Utilisateur(db.Model):
	__tablename__ = "utilisateur"

	code_utilisateur = Column(Integer, primary_key=True)
	nom_utilisateur = Column(String(50), default=None)
	prenom_utilisateur = Column(String(50), default=None)
	username = Column(String(50), default=None)
	couleur_fond_utilisateur = Column(Integer, default=0)
	date_insc_utilisateur = Column(Date)
	Statut=Column(Boolean,default=True)
 


