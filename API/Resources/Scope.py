from API.ApiManager import api
from flask_restplus import Resource , fields
from Database import mongoDb
from flask import jsonify

ns = api.namespace("Scope", "Represents Client Product Scope")

criteria = ns.model('Criteria',
                     {
                         'id':fields.Integer (min=0),'name':fields.String (min=0)}
                     )

@ns.route("/ClientScope/")
class Scope(Resource):
    @ns.doc("From an object return Client object")
    @ns.expect(criteria)
    def post(self):
        collection = mongoDb.db.Clients

        try:
            criterion = api.payload['id']
            s = collection.find_one({'id': api.payload['id']})
        except:
            criterion = api.payload['name']
            s = collection.find_one({'name': api.payload['name']})
        finally:
            if s is not None:
                output = {'id': s['id'], 'name': s['name'], 'products': s['products']}
            else:
                output = "No such clients based on %s",api.payload

        return jsonify(output)

    def get(self):
        obj = []
        collection=mongoDb.db.Clients
        for client in collection.find():
            obj.append(client)
        return jsonify(obj)

