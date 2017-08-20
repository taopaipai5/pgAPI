
from flask_restplus import Api


api = Api(version='0.1', title='Product Governance Audit API',
          description='Retrieve pg activity'
          )


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500
