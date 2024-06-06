import unittest
from app import app


class TestClients(unittest.TestCase):
    def test_get_clients(self):
         with app.test_client() as client:
            response = client.get('/clients')
            self.assertEqual(response.status_code, 200, "Status code != 200")
            expected_data = [ { "CodeCli": 1, 
                               "Nom": "Dupont",
                               "Prenom": "Jean",
                               "Email": "jean.dupont@example.com",
                               "Adresse": "123 Rue de Paris",
                               "IdCodePostal": 75000,
                               "Genre": "Homme" } ]
            self.assertEqual(response.json, expected_data,
                             "La réponse ne correspond pas aux données attendues")

if __name__ == '__main__':
    unittest.main()
    