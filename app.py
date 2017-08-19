import flask
import datetime
from flask_restplus import Resource, Api, fields

app = flask.Flask(__name__)
api = Api(app, version='0.1', title='Product Governance Audit API',
          description='Retrieve pg activity',
          )

app.config.SWAGGER_UI_JSONEDITOR = True

nshello = api.namespace('hello', description='just say hello')

auditparams = api.model('AuditParams', {
    'from_date': fields.String(readOnly=True, description='from where query starts expected format 2017-01-01'),
    'excel_doc_path': fields.String(required=True, description='The task details')
})


@nshello.route("/<string:name>")
class HelloWorld(Resource):
    def get(self, name):
        mystr = 'World'
        if name is not None:
            mystr = name
        return {"Hello": mystr}


ns = api.namespace("ProductGovernance", "Represents audit activity for product governance topic")


@ns.route("/AuditActivity/")
class AuditActivity(Resource):
    @ns.expect(auditparams)
    def post(self):
        """
         Actual request param
        """
        return api.payload


if __name__ == '__main__':
    app.run(debug=True)
