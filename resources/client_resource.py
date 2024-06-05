from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from schemas.client_schema import ClientSchema
from models.client import Client
from globals import api

model_data = {
    "CodeCli": fields.Integer(description="ID du client", example=1),
    "Nom": fields.String(description="Nom du client", example="Dupont", required=True),
    "Prenom": fields.String(description="Prénom du client", example="Jean", required=True),
    "Email": fields.String(description="Adresse mail du client", example="jean.dupont@example.com", required=True),
    "Adresse": fields.String(description="Adresse principale du client", example="123 Rue de Paris"),
    "IdCodePostal": fields.Integer(description="Code Postal de l'adresse du client", example="75000"),
    "Genre": fields.String(description="Homme/Femme", enum=["Homme", "Femme"]),
}

client_model = api.model("Client", model_data)
client_payload = api.model("Client Payload", {k: v for k, v in model_data.items() if k not in ["CodeCli"]})

@api.doc(params={"client_id": "ID du client concerné"}, model=client_model)
class ClientResource(Resource):
    client_schema = ClientSchema()

    # GET
    @api.doc(description="Récupèrer un client par son ID")
    def get(self, client_id):
        client = Client.query.get_or_404(client_id)
        return self.client_schema.dump(client)

    # PUT
    @api.expect(client_payload)
    @api.doc(description="Modifier un client existant")
    def put(self, client_id):
        try:
            new_client_data=self.client_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        client=Client.query.get_or_404(client_id)

        for key, value in new_client_data.items():
            if value is not None:
                setattr(client,key,value)

        db.session.commit()
        return self.client_schema.dump(client)

    #PATCH
    @api.expect(client_payload)
    @api.doc(description="Modifier les attributs d'un client existant")
    def patch(self,client_id):
        try:
            new_client_data = self.client_schema.load(request.json, partial=True)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages}, 400

        client=Client.query.get_or_404(client_id)

        for key, value in new_client_data.items():
            if value is not None:
                setattr(client,key,value)

        db.session.commit()
        return self.client_schema.dump(client)

    # DELETE
    @api.doc(description="Supprimer un client")
    def delete(self,client_id):
        client=Client.query.get_or_404(client_id)
        client.Statut=False
        db.session.commit()
        return self.client_schema.dump(client)

@api.doc(model=client_model)
class ClientListResource(Resource):
    client_schema = ClientSchema()

    # GET
    @api.marshal_with(fields=client_model, as_list=True)
    @api.doc(description="Récuperer la liste de tous les clients")
    def get(self):
        all_clients=Client.query.all()
        return self.client_schema.dump(all_clients, many=True)

    # POST
    @api.expect(client_payload)
    @api.doc(description="Ajouter un nouvel client")
    def post(self):
        try:
            new_client_data = self.client_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        new_client=Client(
            Nom=new_client_data["Nom"],
            Prenom=new_client_data["Prenom"],
            Adresse=new_client_data["Adresse"],
            IdCodePostal=new_client_data["IdCodePostal"],
            Genre=new_client_data["Genre"],
            Email=new_client_data["Email"]
        )

        db.session.add(new_client)
        db.session.commit()
        return self.client_schema.dump(new_client)
