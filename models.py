from flask import Flask
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

class Article(db.Model):
	__tablename__ = "article"

	CodeArticle = Column(Integer, primary_key=True)
	Designation = Column(String(50), default=None)
	Poids = Column(Numeric, default=0.0000)
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
	# couleur_fond_utilisateur = Column(Integer, default=0)
	date_insc_utilisateur = Column(Date)
	



def init_models(app = Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
        clients = [
     	Client(Nom="Durand", Prenom="Jean", Adresse="123 Rue de la Paix", IdCodePostal=75001, Genre="Homme", Email="jean.durand@example.com"),
		Client(Nom="Martin", Prenom="Claire", Adresse="456 Avenue des Champs", IdCodePostal=75008, Genre="Femme", Email="claire.martin@example.com"),
		Client(Nom="Dupont", Prenom="Marie", Adresse="789 Boulevard Saint-Germain", IdCodePostal=75006, Genre="Femme", Email="marie.dupont@example.com")
		]
        articles = [
		Article(Designation="Stylo", Poids=0.05, NbreDePoints=10),
		Article(Designation="Cahier", Poids=0.3, NbreDePoints=20),
		Article(Designation="Sac à dos", Poids=0.5, NbreDePoints=50)
	]
        commandes = [
		Commande(CodeClient=1, DateCde="2023-01-15", MtTotal=100.0, CodeOperateur=1, NSuivi="ABC123", DateExpedition="2023-01-17"),
		Commande(CodeClient=2, DateCde="2023-02-20", MtTotal=150.0, CodeOperateur=2, NSuivi="DEF456", DateExpedition="2023-02-22")
	]
        commande_articles = [
		CommandeArticle(NumCde=1, CodeArticle=1, CodeEmballage=1, CodeModele=1, Poids=0.05, MontantAffranchissement=5.0),
		CommandeArticle(NumCde=1, CodeArticle=2, CodeEmballage=2, CodeModele=2, Poids=0.3, MontantAffranchissement=10.0),
		CommandeArticle(NumCde=2, CodeArticle=3, CodeEmballage=3, CodeModele=3, Poids=0.5, MontantAffranchissement=15.0)
	]
        utilisateurs = [
		Utilisateur(nom_utilisateur="Admin", prenom_utilisateur="Super", username="admin", date_insc_utilisateur="2023-01-01"),
		Utilisateur(nom_utilisateur="User", prenom_utilisateur="Normal", username="user", date_insc_utilisateur="2023-02-01")
	]
 	    # db.session.add(Client(Nom="client1"))
        db.session.bulk_save_objects(clients)
        db.session.bulk_save_objects(articles)
        db.session.bulk_save_objects(commandes)
        db.session.bulk_save_objects(commande_articles)
        db.session.bulk_save_objects(utilisateurs)
        db.session.commit()
	    # db.session.commit()


