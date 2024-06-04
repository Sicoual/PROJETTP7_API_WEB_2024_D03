from flask import request
from flask_restx import Resource
from marshmallow import ValidationError
from models.utilisateur import Utilisateur,db
from schemas.utilisateur_schema import UtilisateurSchema

class UtilisateurResource(Resource):
    
    utilisateur_schema= UtilisateurSchema()
    utilisateur_list_schema = UtilisateurSchema(many=True) #Retourne plusieurs schemas
    utilisateur_patch_schema=UtilisateurSchema(partial=True) #Patch permet de modifier un seul attribut au minimum sans redeclarer le reste
    
    # GET
    def get(self, utilisateur_id=None):
        if utilisateur_id:
            utilisateur=Utilisateur.query.get_or_404(utilisateur_id)
            return self.utilisateur_schema.dump(utilisateur)
        else:
            all_utilisateurs=Utilisateur.query.all()
            return self.utilisateur_list_schema.dump(all_utilisateurs)
        
    # POST
    def post(self):
        try:
            new_utilisateur_data=self.utilisateur_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400
        
        new_utilisateur=Utilisateur(
            nom_utilisateur=new_utilisateur_data["nom_utilisateur"], 
            prenom_utilisateur=new_utilisateur_data["prenom_utilisateur"], 
            username=new_utilisateur_data["username"], 
            couleur_fond_utilisateur=new_utilisateur_data["couleur_fond_utilisateur"], 
            date_insc_utilisateur=new_utilisateur_data["date_insc_utilisateur"], 

        )

        db.session.add(new_utilisateur)
        db.session.commit()
        return self.utilisateur_schema.dump(new_utilisateur)
    
    # PUT
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
    def patch(self,utilisateur_id):
        try:
            new_utilisateur_data=self.utilisateur_patch_schema.load(request.json)
        except ValidationError as err:
            return {"message":"Validation Error", "errors":err.messages},400
        
        utilisateur=Utilisateur.query.get_or_404(utilisateur_id)
        
        for key, value in new_utilisateur_data.items():
            if value is not None:
                setattr(utilisateur,key,value)
                
        db.session.commit()
        return self.utilisateur_schema.dump(utilisateur)
    
    # DELETE
    def delete(self,utilisateur_id):
        utilisateur=Utilisateur.query.get_or_404(utilisateur_id)
        utilisateur.Statut=False
        db.session.commit()
        return self.utilisateur_schema.dump(utilisateur)
