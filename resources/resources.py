from flask_restful import Resource
from models.utilisateur import Utilisateur
from schemas.utilisateur_schema import UtilisateurSchema

class UtilisateurResource(Resource):

    utilisateur_schema = UtilisateurSchema()
    utilisateur_list_schema = UtilisateurSchema(many=True) # Retourne plusieurs schemas

    def get(self, utilisateur_id=None):
        if utilisateur_id:
            utilisateur = Utilisateur.query.get_or_404(utilisateur_id)
            return self.utilisateur_schema.dump(utilisateur)
        else:
            all_utilisateurs = Utilisateur.query.all()
            return self.utilisateur_list_schema.dump(all_utilisateurs)