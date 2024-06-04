from sqlalchemy import (
	Column,
	Float,
	Integer,
	Boolean,
	String
)
from database import db

class Article(db.Model):
	__tablename__ = "article"

	CodeArticle = Column(Integer, primary_key=True)
	Designation = Column(String(50), default=None)
	Poids = Column(Float(), default=0.0000)
	NbreDePoints = Column(Integer, default=0)
	Statut=Column(Boolean,default=True)

