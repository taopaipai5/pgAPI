from API.ApiManager import api
from flask_restplus import Resource

ns = api.namespace('hello', description='just say hello')


@ns.route("/<string:name>")
class HelloWorld(Resource):
    def get(self, name=None):
        mystr = 'World'
        if name is not None:
            mystr = name
        return {"Hello": mystr}
