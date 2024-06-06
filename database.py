from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from os import environ
from dotenv import load_dotenv

load_dotenv()
# Récupération des informations de connexion à partir des variables d'environnement
user = environ.get("DB_USER")
password = environ.get("DB_PASSWORD")
port = environ.get("DB_PORT")
database = environ.get("DB_DATABASE_NAME")
host = environ.get("DB_HOST")

# URL de connexion à la base de données
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user,
    password,
    host,
    port,
    database,
)
# Création de l'engine SQLAlchemy avec les paramètres de connexion
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Déclaration de la base qui permet de créer un modèle et de mapper avec SQLAlchemy
class Base(DeclarativeBase):
    pass

# Initialisation de l'objet SQLAlchemy avec le modèle de base
db = SQLAlchemy(model_class=Base)