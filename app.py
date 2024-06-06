from flask_restx import Namespace
from database import db, SQLALCHEMY_DATABASE_URL
from models.article import Article
from models.client import Client
from models.utilisateur import Utilisateur
from models.commande import Commande
from models.commande_article import CommandeArticle
from datetime import date
from resources.commande_resource import CommandeListResource, CommandeResource
from resources.article_resource import ArticleListResource, ArticleResource
from resources.client_resource import ClientListResource, ClientResource
from resources.utilisateur_resource import UtilisateurListResource, UtilisateurResource
from globals import app, api, ma
from config import TestConfig

#Tests
app.config.from_object(TestConfig)

# Configuration de la base de données
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL
app.config["RESTX_MASK_SWAGGER"] = False
db.init_app(app)

# Initialisation de Marshmallow
ma.init_app(app)

# Configuration de l'API
namespace = Namespace("Client", path="/")
namespace.add_resource(ClientListResource, "/clients")
namespace.add_resource(ClientResource, "/clients/<int:client_id>")
api.add_namespace(namespace)

namespace = Namespace("Article", path="/")
namespace.add_resource(ArticleListResource, "/articles")
namespace.add_resource(ArticleResource, "/articles/<int:article_id>")
api.add_namespace(namespace)

namespace = Namespace("Commande", path="/")
namespace.add_resource(CommandeListResource, "/commandes")
namespace.add_resource(CommandeResource, "/commandes/<int:commande_id>")
api.add_namespace(namespace)

namespace = Namespace("Utilisateur", path="/")
namespace.add_resource(UtilisateurListResource, "/utilisateurs")
namespace.add_resource(UtilisateurResource, "/utilisateurs/<int:utilisateur_id>")
api.add_namespace(namespace)

if __name__ == "__main__":
    # Création de la base de données et ajout des données de test
    with app.app_context():
        try:
            db.drop_all()
            db.create_all()

            # Jeu de données
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
        except Exception as ex:
            print(ex)
    
    # Run the Flask app
    app.run()
