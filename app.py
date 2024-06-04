from flask_restx import Namespace
from database import db, SQLALCHEMY_DATABASE_URL
from models.article import Article 
from models.client import Client 
from models.utilisateur import Utilisateur 
from models.commande import Commande 
from models.commande_article import CommandeArticle
from datetime import date
from resources.commande_resource import CommandeResource
from resources.article_resource import ArticleResource
from resources.client_resource import ClientResource
from resources.utilisateur_resource import UtilisateurResource
from globals import app, api, ma

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL
# BDD
db.init_app(app)
# Mashmallow
ma.init_app(app)
# API
namespace = Namespace("Client", path="/")
namespace.add_resource(ClientResource, "/clients", "/clients/<int:client_id>")
api.add_namespace(namespace)

namespace = Namespace("Article", path="/")
namespace.add_resource(ArticleResource, "/articles", "/articles/<int:article_id>")
api.add_namespace(namespace)

namespace = Namespace("Commande", path="/")
namespace.add_resource(CommandeResource, "/commandes", "/commandes/<int:commande_id>")
api.add_namespace(namespace)

namespace = Namespace("Utilisateur", path="/")
namespace.add_resource(UtilisateurResource, "/utilisateurs", "/utilisateurs/<int:utilisateur_id>")
api.add_namespace(namespace)


with app.app_context():
    try:
        db.drop_all()
        db.create_all()
        #Jeu de données
        client1 = Client(
            Nom="Dupont", 
            Prenom="Jean", 
            Adresse="123 Rue de Paris", 
            IdCodePostal=75000, 
            Genre="Homme", 
            Email="jean.dupont@example.com"

        )
        
        article1 = Article(
            Designation="Stylo", 
            Poids=0.020, 
            NbreDePoints=10
        )
        
        commande1 = Commande(
            CodeClient=1, 
            DateCde=date(2023, 6, 1), 
            MtTotal=100.0, 
            CodeOperateur=1, 
            NSuivi="123456789", 
            DateExpedition=date(2023, 6, 2)
        )
        
        commande_article1 = CommandeArticle(
            NumCde=1, 
            CodeArticle=1, 
            CodeEmballage=1, 
            CodeModele=1, 
            Poids=0.020, 
            MontantAffranchissement=5.0
        )
        
        utilisateur1 = Utilisateur(
            nom_utilisateur="Admin", 
            prenom_utilisateur="Super", 
            username="admin", 
            couleur_fond_utilisateur=0, 
            date_insc_utilisateur=date(2023, 6, 1)
        )

        db.session.add(client1)
        db.session.add(article1)
        db.session.add(commande1)
        db.session.add(commande_article1)
        db.session.add(utilisateur1)

        db.session.commit()
        app.run()
    except Exception as ex:
        print(ex)
