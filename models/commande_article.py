from sqlalchemy import (
	Boolean,
	Column,
	Integer,
	String,
	Date,
	ForeignKey,
	Numeric,
	Float,
)
from database import db



class CommandeArticle(db.Model):
	__tablename__ = "commande_article"

	NumCde = Column(Integer, ForeignKey("commande.NumCde"), primary_key=True)
	CodeArticle = Column(Integer, ForeignKey("article.CodeArticle"), primary_key=True)
	CodeEmballage = Column(Integer)
	CodeModele = Column(Integer)
	Poids = Column(Numeric, default=0.0000)
	MontantAffranchissement = Column(Float, default=0.0000)
	Statut=Column(Boolean,default=True)

