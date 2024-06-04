from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from database import db
from schemas.client_schema import ClientSchema
from models.client import Client
from globals import api

client_model = api.model("Client", {
    'Nom': fields.String(description='Nom du client', example="Dupont", required=True),
    "Prenom": fields.String(description="Prénom du client", example="Jean", required=True),
    'Email': fields.String(description="Adresse mail du client", example="jean.dupont@example.com", required=True),
    'Adresse': fields.String(description='Adresse principale du client', example="123 Rue de Paris"),
    "IdCodePostal": fields.Integer(description="Code Postal de l'adresse du client", example="75000"),
    "Genre": fields.String(enum=["Homme", "Femme"]),
})

class ClientResource(Resource):
    
    client_schema= ClientSchema()
    client_list_schema = ClientSchema(many=True) #Retourne plusieurs schemas
    client_patch_schema=ClientSchema(partial=True) #Patch permet de modifier un seul attribut au minimum sans redeclarer le reste
    
    # GET
    @api.doc(params={'client_id': 'Code du client à afficher'})
    def get(self, client_id=None):
        if client_id:
            client=Client.query.get_or_404(client_id)
            return self.client_schema.dump(client)
        else:
            all_clients=Client.query.all()
            return self.client_list_schema.dump(all_clients)
        
    # POST
    @api.doc(model=client_model)
    def post(self):
        try:
            new_client_data=self.client_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400
        
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
    
    # PUT
    def put(self,client_id):
        try:
            new_client_data=self.client_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400
        
        client=Client.query.get_or_404(client_id)
        
        for key, value in new_client_data.items():
            if value is not None:
                setattr(client,key,value)
                
        db.session.commit()
        return self.client_schema.dump(client)
    
    #PATCH
    @api.doc(params={'client_id': 'Code du client à modifier'})
    def patch(self,client_id):
        try:
            new_client_data=self.client_patch_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400
        
        client=Client.query.get_or_404(client_id)
        
        for key, value in new_client_data.items():
            if value is not None:
                setattr(client,key,value)
                
        db.session.commit()
        return self.client_schema.dump(client)
    
    # DELETE
    @api.doc(params={'client_id': 'Code du client à supprimer'})
    def delete(self,client_id):
        client=Client.query.get_or_404(client_id)
        db.session.delete(client)
        db.session.commit()
        return '',204

    
    
