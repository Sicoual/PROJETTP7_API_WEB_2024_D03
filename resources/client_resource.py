from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from schemas.client_schema import ClientSchema
from models.client import Client
from globals import api

# Définition du modèle Client pour la documentation de l'API
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

"""
Ressource Flask-RESTx pour gérer un client individuel.

Méthodes :
    get(client_id) : Récupère un client par son ID.
    put(client_id) : Met à jour un client existant.
    patch(client_id) : Met à jour partiellement un client existant.
    delete(client_id) : Désactive un client.
"""
@api.doc(params={"client_id": "ID du client concerné"}, model=client_model)
class ClientResource(Resource):
    client_schema = ClientSchema()
   
    @api.doc(description="Récupérer un client par son ID",
             responses={404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID du client n'a pas été renseigné"})
    def get(self, client_id):
        """
        Récupère un client par son ID.

        Paramètres :
            client_id (int) : ID du client à récupérer.

        Retour :
            dict : Données du client.
        """
        client = Client.query.get_or_404(client_id)
        return self.client_schema.dump(client)

    @api.expect(client_payload)
    @api.doc(description="Modifier un client existant",
             responses={400: "Erreur de validation des données", 
                        404: "L'ID renseigné n'existe pas en base de données", 
                        405: "L'ID du client n'a pas été renseigné"})
    def put(self, client_id):
        """
        Met à jour un client existant.

        Paramètres :
            client_id (int) : ID du client à mettre à jour.

        Retour :
            dict : Données du client mis à jour.
        """
        try:
            new_client_data = self.client_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        client = Client.query.get_or_404(client_id)

        for key, value in new_client_data.items():
            if value is not None:
                setattr(client, key, value)

        db.session.commit()
        return self.client_schema.dump(client)

    # PATCH
    @api.expect(client_payload)
    @api.doc(description="Modifier les attributs d'un client existant",
             responses={400: "Erreur de validation des données", 
                        404: "L'ID renseigné n'existe pas en base de données", 
                        405: "L'ID du client n'a pas été renseigné"})
    def patch(self, client_id):
        """
        Met à jour partiellement un client existant.

        Paramètres :
            client_id (int) : ID du client à mettre à jour partiellement.

        Retour :
            dict : Données du client mis à jour partiellement.
        """
        try:
            new_client_data = self.client_schema.load(request.json, partial=True)
        except ValidationError as err:
            return {"message":  "Validation Error", "errors":  err.messages},  400

        client = Client.query.get_or_404(client_id)

        for key, value in new_client_data.items():
            if value is not None:
                setattr(client, key, value)

        db.session.commit()
        return self.client_schema.dump(client)

    # DELETE
    @api.doc(description="Supprimer un client",
             responses={404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID du client n'a pas été renseigné"})
    def delete(self, client_id):
        """
        Désactive un client en mettant son statut à False.

        Paramètres :
            client_id (int) : ID du client à désactiver.

        Retour :
            dict : Données du client désactivé.
        """
        client = Client.query.get_or_404(client_id)
        client.Statut = False
        db.session.commit()
        return self.client_schema.dump(client)

"""
Ressource Flask-RESTx pour gérer la collection de clients.

Méthodes :
    get() : Récupère tous les clients.
    post() : Crée un nouveau client.
"""
@api.doc(model=client_model)
class ClientListResource(Resource):
    client_schema = ClientSchema()

    @api.marshal_with(client_model, as_list=True)
    @api.doc(description="Récupérer la liste de tous les clients",
             responses={404: "Aucun client trouvé"})
    def get(self):
        """
        Récupère tous les clients.

        Retour :
            list : Liste des clients.
        """
        all_clients = Client.query.all()
        if not all_clients:
            return {"message": "Aucun client trouvé"}, 404
        return self.client_schema.dump(all_clients, many=True)

    @api.expect(client_payload)
    @api.doc(description="Ajouter un nouveau client",
             responses={400: "Erreur de validation des données"})
    def post(self):
        """
        Crée un nouveau client.

        Retour :
            dict : Données du nouveau client créé.
        """
        try:
            new_client_data = self.client_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        new_client = Client(
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
