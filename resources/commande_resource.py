from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from models.commande import Commande
from schemas.commande_schema import CommandeSchema
from globals import api

commande_model = api.model("Commande", {
    "NumCde": fields.Integer(description="ID de la commande"),
    "CodeClient": fields.Integer(description="ID du client associé à la commande", required=True),
    "DateCde": fields.Date(description="Date de création de la commande", required=True),
    "MtTotal": fields.Float(description="Montant total de la commande en EUR", required=True),
    "CodeOperateur": fields.Integer(description="Code de l'opérateur associé à la commande"),
    "NSuivi": fields.Integer(description="Numéro de suivi de la commande"),
    "DateExpedition": fields.Date(description="Date d'expédition de la commande"),
})

@api.doc(params={"commande_id": "ID de la commande concernée"}, model=commande_model)
class CommandeResource(Resource):
    commande_schema = CommandeSchema()

    # GET
    def get(self, commande_id):
        commande = Commande.query.get_or_404(commande_id)
        return self.commande_schema.dump(commande)


@api.doc(model=commande_model)
class CommandeListResource(Resource):
    commande_schema = CommandeSchema()

    # GET
    @api.marshal_with(fields=commande_model, as_list=True)
    def get(self):
        all_commandes = Commande.query.all()
        return self.commande_schema.dump(all_commandes, many=True)

    # POST
    @api.doc(model=commande_model)
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
