class Config:
    # configurations par defaut
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'

class TestConfig(Config):
    # Configuration settings for testing environment
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
