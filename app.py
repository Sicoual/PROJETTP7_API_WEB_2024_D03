from flask import Flask
from models import db,Client
from database import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/database_name'
db.init_app(app)


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


