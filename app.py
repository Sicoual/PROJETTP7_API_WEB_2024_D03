<<<<<<< HEAD
from flask import Flask
from models import db,Client
from database import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/database_name'
db.init_app(app)




=======
from flask import Flask, jsonify
from database import db, SQLALCHEMY_DATABASE_URL
from models import init_models, Client
>>>>>>> e4651c04f522ef76d10aeb69c4fcbd76033b458e

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL

db.init_app(app)
init_models(app)

@app.route("/clients")
def clients_all():
    clients = Client.query.all()
    print(clients)
    return jsonify(list(map(lambda el: el.as_dict(), clients)))

<<<<<<< HEAD
with app.app_context():
    db.drop_all    
    db.create_all()

    client = Client(
        Genre="A",
        Nom="B",
        Prenom="V",
        Adresse="123",
        adresse2cli="Lol",
        adresse3cli="",
        villecli_id=1,  
        telcli="123456789",
        emailcli="@mail",
        portcli="0451558555",
        newsletter=1
    )
    db.session.add(new_client)
    db.session.commit()
print(f"Ajouté: {new_client.Nom} {new_client.Prenom}")

app.run()



=======
app.run()
>>>>>>> e4651c04f522ef76d10aeb69c4fcbd76033b458e
