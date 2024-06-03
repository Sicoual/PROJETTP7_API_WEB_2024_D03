from flask_restful import Resource
from models import Client
from schemas import ClientSchema

class ClientResource(Resource):

    client_schema = ClientSchema()
    client_list_schema = ClientSchema(many=True) # Retourne plusieurs schemas

    def get(self, client_id=None):
        if client_id:
            client = Client.query.get_or_404(client_id)
            return self.client_schema.dump(client)
        else:
            all_clients = Client.query.all()
            return self.client_list_schema.dump(all_clients)
