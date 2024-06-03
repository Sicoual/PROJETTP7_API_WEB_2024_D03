from flask import Flask, jsonify
from database import db, SQLALCHEMY_DATABASE_URL
from models import init_models, Client

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL

db.init_app(app)
init_models(app)

@app.route("/clients")
def clients_all():
    clients = Client.query.all()
    print(clients)
    return jsonify(list(map(lambda el: el.as_dict(), clients)))

app.run()
