from functools import partial
from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from models.commande import Commande
from schemas.commande_schema import CommandeSchema
from globals import api

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

@api.doc(params={"commande_id": "ID de la commande concernée"}, model=commande_model)
class CommandeResource(Resource):
    commande_schema = CommandeSchema()

    # GET
    @api.doc(description="Récupérer une commande par son ID",
             responses={404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID de la commande n'a pas été renseigné"})
    def get(self, commande_id):
        commande = Commande.query.get_or_404(commande_id)
        return self.commande_schema.dump(commande)

    # PUT
    @api.expect(commande_payload)
    @api.doc(description="Modifier une commande existante",
             responses={400: "Erreur de validation des données", 404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID de la commande n'a pas été renseigné"})
    def put(self, commande_id):
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

    # PATCH
    @api.expect(commande_payload)
    @api.doc(description="Modifier les attributs d'une commande existante",
             responses={400: "Erreur de validation des données", 404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID de la commande n'a pas été renseigné"})
    def patch(self, commande_id):
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

    # DELETE
    @api.doc(description="Supprimer une commande",
             responses={404: "L'ID renseigné n'existe pas en base de données", 405: "L'ID de la commande n'a pas été renseigné"})
    def delete(self, commande_id):
        commande = Commande.query.get_or_404(commande_id)
        commande.Statut = False
        db.session.commit()
        return self.commande_schema.dump(commande)

@api.doc(model=commande_model)
class CommandeListResource(Resource):
    commande_schema = CommandeSchema()

    # GET
    @api.marshal_with(commande_model, as_list=True)
    @api.doc(description="Récupérer la liste de toutes les commandes",
             responses={404: "Aucune commande trouvée"})
    def get(self):
        all_commandes = Commande.query.all()
        if not all_commandes:
            return {"message": "Aucune commande trouvée"}, 404
        return self.commande_schema.dump(all_commandes, many=True)

    # POST
    @api.expect(commande_payload)
    @api.doc(description="Ajouter une nouvelle commande",
             responses={400: "Erreur de validation des données"})
    def post(self):
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
