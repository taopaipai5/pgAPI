from API.ApiManager import api
from flask_restplus import Resource, fields
import re
import uuid


params = api.model('RegexParams', {
    'mystring': fields.String(readOnly=True, description='string to apply the pattern to')
})

ns = api.namespace('RegExSample', description='RegexTest')



@ns.route("/")
class RegExSample(Resource):
    @ns.expect(params)
    def post(self):
        regexp = r"<quoteRequestId>\w{8}-\w{4}-\w{4}-\w{4}-\w{12}</quoteRequestId>"
        p = re.compile(regexp)
        print(api.payload['mystring'])

        if p.search(api.payload['mystring']) is not None:
            newstr = p.sub("<quoteRequestId>" + str(uuid.uuid4()) + "</quoteRequestId>", api.payload['mystring'], 1)
            return newstr
        else:
            return "No match"