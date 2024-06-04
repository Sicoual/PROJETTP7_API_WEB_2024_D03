from flask import Flask
from database import db, SQLALCHEMY_DATABASE_URL
from models import init_models

# fonctions get_
from endpoints.clients import get_clients
from endpoints.articles import get_articles
from endpoints.commandes import get_commandes
from endpoints.commande_articles import get_commande_articles
from endpoints.utilisateurs import get_utilisateurs

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL

db.init_app(app)
init_models(app)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# Define routes and link to imported functions
@app.route("/clients")
def clients_route():
    return get_clients()

@app.route("/articles")
def articles_route():
    return get_articles()

@app.route("/commandes")
def commandes_route():
    return get_commandes()

@app.route("/commande_articles")
def commande_articles_route():
    return get_commande_articles()

@app.route("/utilisateurs")
def utilisateurs_route():
    return get_utilisateurs()

if __name__ == "__main__":
    with app.app_context():
        init_models(app)
        app.run()
