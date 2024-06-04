from sqlalchemy import (
	Column,
	Integer,
	String,
	Date,
	ForeignKey,
	Float,
)
from database import db


class Commande(db.Model):
	__tablename__ = "commande"

	NumCde = Column(Integer, primary_key=True)
	CodeClient = Column(Integer, ForeignKey("client.CodeCli"))
	DateCde = Column(Date)
	MtTotal = Column(Float)
	CodeOperateur = Column(Integer)
	NSuivi = Column(String(50), default=None)
	DateExpedition = Column(Date)
