from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

app.config.from_object("app.config.DevelopmentConfig")

from app.beers import beer