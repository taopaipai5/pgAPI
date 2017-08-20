from API.ApiManager import api
from flask_restplus import Resource , fields

auditparams = api.model('AuditParams', {
    'from_date': fields.String(readOnly=True, description='from where query starts expected format 2017-01-01'),
    'excel_doc_path': fields.String(required=True, description='The task details')
})

ns = api.namespace("ProductGovernance", "Represents audit activity for product governance topic")

@ns.route("/AuditActivity/")
class AuditActivity(Resource):
    @ns.expect(auditparams)
    def post(self):
        """
         Actual request param
        """
        return api.payload

