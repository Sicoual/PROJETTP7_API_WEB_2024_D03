from flask import request
from flask_restx import Resource
from marshmallow import ValidationError
from models.commande import Commande,db
from schemas.commande_schema import CommandeSchema

class CommandeResource(Resource):
    commande_schema = CommandeSchema()

    # GET
    def get(self, commande_id):
        commande = Commande.query.get_or_404(commande_id)
        return self.commande_schema.dump(commande)


class CommandeListResource(Resource):
    commande_schema = CommandeSchema()

    # GET
    def get(self):
        all_commandes = Commande.query.all()
        return self.commande_schema.dump(all_commandes, many=True)

    # POST
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
