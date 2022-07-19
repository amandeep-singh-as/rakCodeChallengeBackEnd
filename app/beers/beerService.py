import os
from urllib import response
import requests
from flask import make_response, jsonify

class BeerService:
    beerUri = os.environ.get('BEERS')
    beer = []

    def getBeers(self):
        page = 1
        while True:
            response = requests.get(self.beerUri + '/beers?page=' + str(page) + '&per_page=80')
            data = response.json()
            if(len(data) <= 0):
                return
            for b in data:
                self.beer.append(b)
            page += 1

    def getAllBeers(self):
        if(len(self.beer) == 0):
            self.getBeers()
        return make_response(jsonify(
            success= True,
            data = self.beer
        ), 200)

    def getTopFermentedBeer(self):
        if(len(self.beer) == 0):
            self.getBeers()
        topFermentedBeer = []
        for b in self.beer:
            if((b['method']['fermentation']['temp']['value'] != None) and (b['method']['fermentation']['temp']['value'] >= 10 and 
            b['method']['fermentation']['temp']['value'] <= 25)):
                topFermentedBeer.append(b)
        return make_response(jsonify(
            success = True,
            data = topFermentedBeer
        ), 200)

    def getBottomFermentedBeer(self):
        if(len(self.beer) == 0):
            self.getBeers()
        bottomFermentedBeer = []
        for b in self.beer:
            if((b['method']['fermentation']['temp']['value'] != None) and (b['method']['fermentation']['temp']['value'] >= 7 and b['method']['fermentation']['temp']['value'] <= 15)):
                bottomFermentedBeer.append(b)
        return make_response(jsonify(
            success = True,
            data = bottomFermentedBeer
        ), 200)

    def getBeerByBitterness(self, bitterness):
        if(len(self.beer) == 0):
            self.getBeers()
        beerByBitterness = []
        for b in self.beer:
            if(b['ibu'] != None and b['ibu'] == int(bitterness)):

                beerByBitterness.append(b)
        return make_response(jsonify(
            success = True,
            data = beerByBitterness
        ), 200)
beerService = BeerService()