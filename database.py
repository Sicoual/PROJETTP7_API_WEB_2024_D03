from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import Client
from database import Base
# connexion a la base de donnée et déclaration de la base avec sql alchemy

user = environ.get("DB_USER")
password = environ.get("DB_PASSWORD")
port = environ.get("DB_PORT")
database = environ.get("DB_DATABASE_NAME")
host = environ.get("DB_HOST")

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user,
    password,
    host,
    port,
    database,
)

# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
class Base(DeclarativeBase):
    pass

# creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
