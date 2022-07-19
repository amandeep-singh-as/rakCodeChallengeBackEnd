from urllib import response
from flask import Blueprint, jsonify, request
import os
from dotenv import load_dotenv
from app import app

load_dotenv()

from app.beers.beerService import beerService

beer = Blueprint(name = 'beer', import_name = __name__)

@beer.route('/beers')
def getBeers():
    response = beerService.getAllBeers()
    return response

@beer.route('/topfermentedbeers')
def getTopFermentedBeers():
    response = beerService.getTopFermentedBeer()
    return response

@beer.route('/bottomfermentedbeers')
def getBottomFermentedBeers():
    response = beerService.getBottomFermentedBeer()
    return response

@beer.route('/beerbybitterness')
def getBeerByBitterness():
    bitterness = request.args.get('bitterness')
    print(bitterness)
    response = beerService.getBeerByBitterness(bitterness = bitterness)
    return response

app.register_blueprint(beer, url_prefix="/api")