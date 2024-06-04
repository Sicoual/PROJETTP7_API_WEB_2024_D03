from flask import jsonify
from models import Commande

def get_commandes():
    commandes = Commande.query.all()
    commandes_list = [
        {
            "NumCde": commande.NumCde,
            "CodeClient": commande.CodeClient,
            "DateCde": commande.DateCde.isoformat() if commande.DateCde else None,
            "MtTotal": commande.MtTotal,
            "CodeOperateur": commande.CodeOperateur,
            "NSuivi": commande.NSuivi,
            "DateExpedition": commande.DateExpedition.isoformat() if commande.DateExpedition else None
        }
        for commande in commandes
    ]
    return jsonify(commandes_list)
