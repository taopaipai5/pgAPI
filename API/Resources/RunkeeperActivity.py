from API.ApiManager import api
from flask_restplus import Resource
import requests

ns = api.namespace('RunKeeper', description='My Runkeeper Activity')


@ns.route("/<string:access_token>")
class FitnessActivityRunKeeper(Resource):
    def get(self,access_token):
        payload = {'access_token': access_token}
        r = requests.get('https://api.runkeeper.com/fitnessActivities', payload)
        return r.json(),r.status_code
