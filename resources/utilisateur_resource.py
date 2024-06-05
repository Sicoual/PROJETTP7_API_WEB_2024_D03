from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from models.utilisateur import Utilisateur
from database import db
from schemas.utilisateur_schema import UtilisateurSchema
from globals import api

model_data = {
    "code_utilisateur": fields.Integer(description="ID de l'utilisateur", example=1),
    "nom_utilisateur": fields.Integer(description="Nom de famille de l'utilisateur", required=True),
    "prenom_utilisateur": fields.Date(description="Prénom de l'utilisateur", required=True),
    "username": fields.Float(description="Pseudonyme de l'utilisateur", required=True),
    "couleur_fond_utilisateur": fields.Integer(description=""),
    "date_insc_utilisateur": fields.Integer(description="Date d'inscription de l'utilisateur"),
}

utilisateur_model = api.model("Utilisateur", model_data)
utilisateur_payload = api.model("Utilisateur Payload", {k: v for k, v in model_data.items() if k not in ["code_utilisateur"]})

@api.doc(params={"utilisateur_id": "ID de l'utilisateur concerné"}, model=utilisateur_model)
class UtilisateurResource(Resource):
    utilisateur_schema = UtilisateurSchema()

    # GET
    @api.doc(description="Récupèrer un utilisateur par son ID")
    def get(self, utilisateur_id=None):
        utilisateur=Utilisateur.query.get_or_404(utilisateur_id)
        return self.utilisateur_schema.dump(utilisateur)

    # PUT
    @api.expect(utilisateur_payload)
    @api.doc(description="Modifier un utilisateur existant")
    def put(self,utilisateur_id):
        try:
            new_utilisateur_data=self.utilisateur_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400

        utilisateur=Utilisateur.query.get_or_404(utilisateur_id)

        for key, value in new_utilisateur_data.items():
            if value is not None:
                setattr(utilisateur,key,value)

        db.session.commit()
        return self.utilisateur_schema.dump(utilisateur)

    #PATCH
    @api.expect(utilisateur_payload)
    @api.doc(description="Modifier les attributs d'un utilisateur existant")
    def patch(self,utilisateur_id):
        try:
            new_utilisateur_data = self.utilisateur_schema.load(request.json, partial=True)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages}, 400

        utilisateur=Utilisateur.query.get_or_404(utilisateur_id)

        for key, value in new_utilisateur_data.items():
            if value is not None:
                setattr(utilisateur, key,value)

        db.session.commit()
        return self.utilisateur_schema.dump(utilisateur)

    # DELETE
    @api.doc(description="Supprimer un utilisateur")
    def delete(self,utilisateur_id):
        utilisateur=Utilisateur.query.get_or_404(utilisateur_id)
        utilisateur.Statut=False
        db.session.commit()
        return self.utilisateur_schema.dump(utilisateur)


@api.doc(model=utilisateur_model)
class UtilisateurListResource(Resource):
    utilisateur_schema = UtilisateurSchema()

    # GET
    @api.marshal_with(fields=utilisateur_model, as_list=True)
    @api.doc(description="Récuperer la liste de tous les utilisateurs")
    def get(self):
        all_utilisateurs = Utilisateur.query.all()
        return self.utilisateur_schema.dump(all_utilisateurs, many=True)

    # POST
    @api.expect(utilisateur_payload)
    @api.doc(description="Ajouter un nouvel utilisateur")
    def post(self):
        try:
            new_utilisateur_data=self.utilisateur_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation Error", "errors": err.messages},400

        new_utilisateur = Utilisateur(
            nom_utilisateur=new_utilisateur_data["nom_utilisateur"],
            prenom_utilisateur=new_utilisateur_data["prenom_utilisateur"],
            username=new_utilisateur_data["username"],
            couleur_fond_utilisateur=new_utilisateur_data["couleur_fond_utilisateur"],
            date_insc_utilisateur=new_utilisateur_data["date_insc_utilisateur"],
        )

        db.session.add(new_utilisateur)
        db.session.commit()
        return self.utilisateur_schema.dump(new_utilisateur)
