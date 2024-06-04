from sqlalchemy import (
	Boolean,
	Column,
	Integer,
	String,
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
	Statut=Column(Boolean,default=True)
