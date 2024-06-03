<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float, MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship,declarative_base
from database import Base, engine


Base = declarative_base()
db = SQLAlchemy(model_class=Base)

class Client(Base):
=======
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
>>>>>>> e4651c04f522ef76d10aeb69c4fcbd76033b458e
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

<<<<<<< HEAD
class Commune(Base):
	_tablename__ = "t_communes"

	id = Column(Integer,primary_key=True)
	dep = Column(Integer,ForeignKey('t_dept.code_dept'))
	cp = Column(String(5), default=None)
ville = Column(String(50), default=None)
=======
	CodeArticle = Column(Integer, primary_key=True)
	Designation = Column(String(50), default=None)
	Poids = Column(Numeric, default=0.0000)
	NbreDePoints = Column(Integer, default=0)

class Commande(db.Model):
	__tablename__ = "commande"
>>>>>>> e4651c04f522ef76d10aeb69c4fcbd76033b458e

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

def init_models(app = Flask):
	with app.app_context():
		db.drop_all()
		db.create_all()

<<<<<<< HEAD
# class Commande(Base):
# 	__tablename__ = "t_entcde"

# 	codcde = Column(Integer,primary_key=True)
# 	datcde = Column(Date)
# 	codcli = Column(Integer,ForeignKey('t_client.codcli'))
# 	timbrecli = Column(Float)
# 	timbrecde = Column(Float)
# 	nbcolis = Column(Integer, default=1)
# 	cheqcli = Column(Float)
# 	idcondit = Column(Integer, default=0)
# 	cdeComt = Column(String(255), default=None)
# 	barchive = Column(Integer, default=0)
# 	bstock = Column(Integer, default=0)

# 	__table_args__ = (Index('commmande_index', "cdeComt", "codcli"),)

# class Conditionnement(Base):
# 	__tablename__ = "t_conditionnement"

# 	idcondit = Column(Integer,primary_key=True)
# 	libcondit = Column(String(50), default=None)
# 	poidscondit = Column(Integer)
# 	prixcond = Column(Numeric, default=0.0000)
# 	ordreimp = Column(Integer)
# 	# codobj = Column(Integer, ForeignKey('t_objet.codobj'))
# 	objets = relationship("ObjetCond",back_populates='condit')

# class Objet(Base):
# 	__tablename__ = "t_objet"

# 	codobj = Column(Integer,primary_key=True)
# 	libobj = Column(String(50), default=None)
# 	tailleobj = Column(String(50), default=None)
# 	puobj = Column(Numeric, default=0.0000)
# 	poidsobj = Column(Numeric, default=0.0000)
# 	indispobj = Column(Integer, default=0)
# 	o_imp = Column(Integer, default=0)
# 	o_aff = Column(Integer, default=0)
# 	o_cartp = Column(Integer, default=0)
# 	points = Column(Integer, default=0)
# 	o_ordre_aff = Column(Integer, default=0)
# 	condit = relationship("ObjetCond",back_populates='objets')

# class ObjetCond(Base):
# 	__tablename__ = "t_rel_cond"

# 	idrelcond = Column(Integer,primary_key=True, index=True)
# 	qteobjdeb = Column(Integer, default=0)
# 	qteobjfin = Column(Integer, default=0)
# 	codobj = Column(Integer, ForeignKey('t_objet.codobj'))
# 	codcond = Column(Integer, ForeignKey('t_conditionnement.idcondit'))
# 	objets = relationship("Objet",back_populates='condit')
# 	condit = relationship("Conditionnement",back_populates='objets')

# class Detail(Base):
# 	__tablename__ = "t_dtlcode"

# 	id = Column(Integer,primary_key=True)
# 	codcde = Column(Integer,ForeignKey('t_entcde.codcde'), index=True)
# 	qte = Column(Integer, default=1)
# 	colis = Column(Integer, default=1)
# 	commentaire = Column(String(100), default=None)

# class DetailObjet(Base):
# 	__tablename__ = "t_dtlcode_codobj"

# 	id = Column(Integer,primary_key=True)
# 	detail_id = Column(Integer, ForeignKey('t_dtlcode.id'))
# 	objet_id = Column(Integer, ForeignKey('t_objet.codobj'))

# class Enseigne(Base):
# 	__tablename__ = "t_enseigne"

# 	id_enseigne = Column(Integer,primary_key=True)
# 	lb_enseigne = Column(String(50), default=None)
# 	ville_enseigne = Column(String(50), default=None)
# 	dept_enseigne = Column(Integer, default=0)



# class Poids(Base):
# 	__tablename__ = "t_poids"

# 	id = Column(Integer,primary_key=True)
# 	valmin = Column(Numeric, default=0)
# 	valtimbre = Column(Numeric, default=0)

# class Vignette(Base):
# 	__tablename__ = "t_poidsv"

# 	id = Column(Integer,primary_key=True)
# 	valmin = Column(Numeric, default=0)
# 	valtimbre = Column(Numeric, default=0)


# class Role(Base):
# 	__tablename__ = "t_role"

# 	codrole= Column(Integer,primary_key=True)
# 	librole = Column(String(25), default=None)


# class Utilisateur(Base):
# 	__tablename__ = "t_utilisateur"

# 	code_utilisateur = Column(Integer,primary_key=True)
# 	nom_utilisateur = Column(String(50), default=None)
# 	prenom_utilisateur = Column(String(50), default=None)
# 	username = Column(String(50), default=None)
# 	couleur_fond_utilisateur = Column(Integer, default=0)
# 	date_insc_utilisateur = Column(Date)

# class RoleUtilisateur(Base):
# 	__tablename__ = "t_utilisateur_role"

# 	id = Column(Integer,primary_key=True)
# 	utilisateur_id = Column(Integer, ForeignKey('t_utilisateur.code_utilisateur'))
# 	role_id = Column(Integer, ForeignKey('t_role.codrole'))

Base.metadata.create_all(engine)

=======
		db.session.add(Client(Nom="client1"))
		db.session.commit()
>>>>>>> e4651c04f522ef76d10aeb69c4fcbd76033b458e
