# Flask API Application

## Description

Cette application est une API RESTful construite avec Flask. Elle permet de gérer des ressources via des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer).

## Structure du Projet

Le projet est organisé comme suit :

    ├── app.py
    ├── database.py
    ├── globals.py
    ├── models
    │ └── (fichiers de modèles de données)
    ├── resources
    │ └── (fichiers de gestion des endpoints)
    ├── schemas
    │ └── (fichiers de schémas de validation)
    ├── requirements.txt

- **app.py** : Point d'entrée de l'application Flask.
- **database.py** : Configuration de la base de données avec SQLAlchemy.
- **globals.py** : Configuration globale et variables partagées.
- **models/** : Contient les fichiers de modèles de données.
- **resources/** : Contient les fichiers de gestion des endpoints de l'API.
- **schemas/** : Contient les fichiers de schémas de validation pour les données.
- **requirements.txt** : Liste des dépendances nécessaires pour exécuter l'application.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés :

- Python 3.6 ou supérieur
- pip (gestionnaire de paquets Python)
- virtualenv (recommandé)

## Installation

1. Clonez le dépôt :
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo

2. Créez un environnement virtuel et activez-le :
   python -m venv env
   source env/bin/activate # Sur Windows: .\env\Scripts\activate

3. Installez les dépendances :
   pip install -r requirements.txt

# Utilisation

1. Lancement du serveur
   Pour démarrer le serveur Flask, exécutez la commande suivante :
   flask run ou python app.py
   Le serveur sera accessible sur http://127.0.0.1:5000/.

### Endpoints

Voici une liste des exemples pour des endpoints disponibles avec une brève description de leur fonction :

#### Client Resource Endpoints :

- `GET /clients` : Récupère la liste de tous les clients.
- `GET /clients/<id>` : Récupère les détails d'un client spécifique par son ID.
- `POST /clients` : Crée un nouveau client.
  - Body (JSON) : `{ "name": "Nom du client", "email": "Email du client" }`
- `PUT /clients/<id>` : Met à jour un client existant par son ID.
  - Body (JSON) : `{ "name": "Nom mis à jour", "email": "Email mis à jour" }`
- `PATCH /clients/<id>` : Met à jour partiellement un client existant par son ID.
  - Body (JSON) : `{ "name": "Nom partiellement mis à jour", "email": "Email partiellement mis à jour" }`
- `DELETE /clients/<id>` : Désactive un client par son ID.


## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.



## Auteurs

- Ilyes
- Dorian
- Zaid
- Robin
- Macron

Ce README inclut toutes les informations nécessaires pour installer, utiliser, et contribuer à votre projet Flask API, ainsi que des exemples de requêtes pour les différents endpoints.