from flask import jsonify
from models import Utilisateur

def get_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    utilisateurs_list = [
        {
            "code": utilisateur.code_utilisateur,
            "nom": utilisateur.nom_utilisateur,
            "prenom": utilisateur.prenom_utilisateur
        }
        for utilisateur in utilisateurs
    ]
    return jsonify(utilisateurs_list)
