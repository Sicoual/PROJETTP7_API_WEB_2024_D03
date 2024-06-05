import pytest
from flask import Flask
from database import db  
from models.client import Client
from database import db, SQLALCHEMY_DATABASE_URL


@pytest.fixture(scope='module')
def client():
    """
    Create a test client for the Flask app.
    This is a fixture that will be used in the tests.
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL
    app.config['TESTING'] = True
    app.debug = True
    # BDD
    db.init_app(app)
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
            
            # article1 = Article(
            #     Designation="Stylo", 
            #     Poids=0.020, 
            #     NbreDePoints=10
            # )
            
            # commande1 = Commande(
            #     CodeClient=1, 
            #     DateCde=date(2023, 6, 1), 
            #     MtTotal=100.0, 
            #     CodeOperateur=1, 
            #     NSuivi="123456789", 
            #     DateExpedition=date(2023, 6, 2)
            # )
            
            # commande_article1 = CommandeArticle(
            #     NumCde=1, 
            #     CodeArticle=1, 
            #     CodeEmballage=1, 
            #     CodeModele=1, 
            #     Poids=0.020, 
            #     MontantAffranchissement=5.0
            # )
            
            # utilisateur1 = Utilisateur(
            #     nom_utilisateur="Admin", 
            #     prenom_utilisateur="Super", 
            #     username="admin", 
            #     couleur_fond_utilisateur=0, 
            #     date_insc_utilisateur=date(2023, 6, 1)
            # )

            db.session.add(client1)
            # db.session.add(article1)
            # db.session.add(commande1)
            # db.session.add(commande_article1)
            # db.session.add(utilisateur1)

            db.session.commit()
            app.run()
            client = app.test_client()
            yield client
        except Exception as ex:
            print(ex)

     
    
    

  

def test_get_clients(client):
    response = client.get('/clients/1')
    data = response.json
    print(data)
    # assert response.status_code == 200
    assert isinstance(data, list)
    assert data["Nom"] == "Dupont"
    assert data["Prenom"] == "Jean"
    

