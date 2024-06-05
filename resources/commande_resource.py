from functools import partial
from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from models.commande import Commande
from schemas.commande_schema import CommandeSchema
from globals import api

# Definition of the Commande model for the API documentation
model_data = {
    "NumCde": fields.Integer(description="ID de la commande", example=1),
    "CodeClient": fields.Integer(description="ID de la commande associé à la commande", required=True),
    "DateCde": fields.Date(description="Date de création de la commande", required=True),
    "MtTotal": fields.Float(description="Montant total de la commande en EUR", required=True),
    "CodeOperateur": fields.Integer(description="Code de l'opérateur associé à la commande"),
    "NSuivi": fields.Integer(description="Numéro de suivi de la commande"),
    "DateExpedition": fields.Date(description="Date d'expédition de la commande"),
}

commande_model = api.model("Commande", model_data)
commande_payload = api.model("Commande Payload", {k: v for k, v in model_data.items() if k not in ["NumCde"]})

"""
Ressource Flask-RESTx pour gérer une commande individuelle.

Méthodes :
    get(commande_id) : Récupère une commande par son ID.
    put(commande_id) : Met à jour une commande existante.
    patch(commande_id) : Met à jour partiellement une commande existante.
    delete(commande_id) : Désactive une commande.
"""
@api.doc(params={"commande_id": "ID de la commande concernée"}, model=commande_model)
class CommandeResource(Resource):

    commande_schema = CommandeSchema()

    @api.doc(description="Récupèrer une commande par son ID", responses={405: "L'ID de la commande n'a pas été renseigné"})
    def get(self, commande_id):
        """
        Récupère une commande par son ID.

        Paramètres :
            commande_id (int) : ID de la commande à récupérer.

        Retour :
            dict : Données de la commande.
        """
        commande = Commande.query.get_or_404(commande_id)
        return self.commande_schema.dump(commande)


    @api.expect(commande_payload)
    @api.doc(description="Modifier une commande existante", responses={405: "L'ID de la commande n'a pas été renseigné"})
    def put(self, commande_id):
        """
        Met à jour une commande existante.

        Paramètres :
            commande_id (int) : ID de la commande à mettre à jour.

        Retour :
            dict : Données de la commande mise à jour.
        """
        try:
            new_commande_data = self.commande_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        commande = Commande.query.get_or_404(commande_id)

        for key, value in new_commande_data.items():
            if value is not None:
                setattr(commande, key, value)

        db.session.commit()
        return self.commande_schema.dump(commande)

    @api.expect(commande_payload)
    @api.doc(description="Modifier les attributs d'une commande existante", responses={405: "L'ID de la commande n'a pas été renseigné"})
    def patch(self, commande_id):
        """
        Met à jour partiellement une commande existante.

        Paramètres :
            commande_id (int) : ID de la commande à mettre à jour partiellement.

        Retour :
            dict : Données de la commande mise à jour partiellement.
        """
        try:
            new_commande_data = self.commande_schema.load(request.json, partial=True)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        commande = Commande.query.get_or_404(commande_id)

        for key, value in new_commande_data.items():
            if value is not None:
                setattr(commande, key, value)

        db.session.commit()
        return self.commande_schema.dump(commande)

    @api.doc(description="Supprimer une commande", responses={405: "L'ID de la commande n'a pas été renseigné"})
    def delete(self, commande_id):
        """
        Désactive une commande en mettant son statut à False.

        Paramètres :
            commande_id (int) : ID de la commande à désactiver.

        Retour :
            dict : Données de la commande désactivée.
        """
        commande = Commande.query.get_or_404(commande_id)
        commande.Statut = False
        db.session.commit()
        return self.commande_schema.dump(commande)


"""
Ressource Flask-RESTx pour gérer la collection de commandes.

Méthodes :
    get() : Récupère toutes les commandes.
    post() : Crée une nouvelle commande.
"""
@api.doc(model=commande_model)
class CommandeListResource(Resource):
    commande_schema = CommandeSchema()

    @api.marshal_with(fields=commande_model, as_list=True)
    @api.doc(description="Récuperer la liste de toutes les commandes")
    def get(self):
        """
        Récupère toutes les commandes.

        Retour :
            list : Liste des commandes.
        """
        all_commandes = Commande.query.all()
        return self.commande_schema.dump(all_commandes, many=True)

    @api.expect(commande_payload)
    @api.doc(description="Ajouter une nouvelle commande")
    def post(self):
        """
        Crée une nouvelle commande.

        Retour :
            dict : Données de la nouvelle commande créée.
        """
        try:
            new_commande_data = self.commande_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        new_commande = Commande(
            CodeClient=new_commande_data["CodeClient"],
            DateCde=new_commande_data["DateCde"],
            MtTotal=new_commande_data["MtTotal"],
            CodeOperateur=new_commande_data["CodeOperateur"],
            NSuivi=new_commande_data.get("NSuivi", None),
            DateExpedition=new_commande_data.get("DateExpedition", None),
        )

        db.session.add(new_commande)
        db.session.commit()
        return self.commande_schema.dump(new_commande)
