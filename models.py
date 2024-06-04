from sqlalchemy import (
	Column,
	Integer,
	String,
	Date,
	ForeignKey,
	Numeric,
	Float,
)
from database import db

class Client(db.Model):
	__tablename__ = "client"

	CodeCli = Column(Integer, primary_key=True)
	Nom = Column(String(40), default=None, index=True)
	Prenom = Column(String(30), default=None)
	Adresse = Column(String(50), default=None)
	IdCodePostal = Column(Integer, default=None)
	Genre = Column(String(8), default=None)
	Email = Column(String(255), default=None)

	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Article(db.Model):
	__tablename__ = "article"

	CodeArticle = Column(Integer, primary_key=True)
	Designation = Column(String(50), default=None)
	Poids = Column(Float, default=0.0000)
	NbreDePoints = Column(Integer, default=0)

class Commande(db.Model):
	__tablename__ = "commande"

	NumCde = Column(Integer, primary_key=True)
	CodeClient = Column(Integer, ForeignKey("client.CodeCli"))
	DateCde = Column(Date)
	MtTotal = Column(Float)
	CodeOperateur = Column(Integer)
	NSuivi = Column(String(50), default=None)
	DateExpedition = Column(Date)

class CommandeArticle(db.Model):
	__tablename__ = "commande_article"

	NumCde = Column(Integer, ForeignKey("commande.NumCde"), primary_key=True)
	CodeArticle = Column(Integer, ForeignKey("article.CodeArticle"), primary_key=True)
	CodeEmballage = Column(Integer)
	CodeModele = Column(Integer)
	Poids = Column(Numeric, default=0.0000)
	MontantAffranchissement = Column(Float, default=0.0000)

class Utilisateur(db.Model):
	__tablename__ = "utilisateur"

	code_utilisateur = Column(Integer, primary_key=True)
	nom_utilisateur = Column(String(50), default=None)
	prenom_utilisateur = Column(String(50), default=None)
	username = Column(String(50), default=None)
	couleur_fond_utilisateur = Column(Integer, default=0)
	date_insc_utilisateur = Column(Date)
