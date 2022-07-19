from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = False
    BEERS = "https://api.punkapi.com/v2/"

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True 