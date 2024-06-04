from flask import jsonify
from models import Client

def get_clients():
    clients = Client.query.all()
    clients_list = [
        {
            "CodeCli": client.CodeCli,
            "Nom": client.Nom,
            "Prenom": client.Prenom
        }
        for client in clients
    ]
    return jsonify(clients_list)
