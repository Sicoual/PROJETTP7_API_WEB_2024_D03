swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "My API",
        "description": "API documentation for my Flask application",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"],
    "paths": {
        "/clients": {
            "get": {
                "summary": "Get Clients",
                "responses": {
                    "200": {
                        "description": "A list of clients",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "CodeCli": {
                                        "type": "integer",
                                        "description": "The client code"
                                    },
                                    "Nom": {
                                        "type": "string",
                                        "description": "The client's last name"
                                    },
                                    "Prenom": {
                                        "type": "string",
                                        "description": "The client's first name"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/articles": {
            "get": {
                "summary": "Get Articles",
                "responses": {
                    "200": {
                        "description": "A list of articles",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "CodeArticle": {
                                        "type": "integer",
                                        "description": "The article code"
                                    },
                                    "Designation": {
                                        "type": "string",
                                        "description": "The article designation"
                                    },
                                    "Poids": {
                                        "type": "string",
                                        "description": "The article weight"
                                    },
                                    "NbreDePoints": {
                                        "type": "integer",
                                        "description": "The number of points for the article"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/commandes": {
            "get": {
                "summary": "Get Commandes",
                "responses": {
                    "200": {
                        "description": "A list of commandes",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "NumCde": {
                                        "type": "integer",
                                        "description": "The command number"
                                    },
                                    "CodeClient": {
                                        "type": "integer",
                                        "description": "The client code"
                                    },
                                    "DateCde": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "The command date"
                                    },
                                    "MtTotal": {
                                        "type": "number",
                                        "format": "float",
                                        "description": "The total amount"
                                    },
                                    "CodeOperateur": {
                                        "type": "integer",
                                        "description": "The operator code"
                                    },
                                    "NSuivi": {
                                        "type": "string",
                                        "description": "The tracking number"
                                    },
                                    "DateExpedition": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "The expedition date"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/commande_articles": {
            "get": {
                "summary": "Get Commande Articles",
                "responses": {
                    "200": {
                        "description": "A list of commande articles",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "NumCde": {
                                        "type": "integer",
                                        "description": "The command number"
                                    },
                                    "CodeArticle": {
                                        "type": "integer",
                                        "description": "The article code"
                                    },
                                    "CodeEmballage": {
                                        "type": "integer",
                                        "description": "The packaging code"
                                    },
                                    "CodeModele": {
                                        "type": "integer",
                                        "description": "The model code"
                                    },
                                    "Poids": {
                                        "type": "string",
                                        "description": "The weight"
                                    },
                                    "MontantAffranchissement": {
                                        "type": "number",
                                        "format": "float",
                                        "description": "The postage amount"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/utilisateurs": {
            "get": {
                "summary": "Get Utilisateurs",
                "responses": {
                    "200": {
                        "description": "A list of utilisateurs",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "code": {
                                        "type": "integer",
                                        "description": "The user code"
                                    },
                                    "nom": {
                                        "type": "string",
                                        "description": "The user's last name"
                                    },
                                    "prenom": {
                                        "type": "string",
                                        "description": "The user's first name"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
