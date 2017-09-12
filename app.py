import flask
import settings
from flask import Blueprint

from API.ApiManager import api
from API.Resources.Hello import ns as nsHello
from API.Resources.AuditActivity import ns as nsAudit
from API.Resources.RunkeeperActivity import ns as nsRunKeeper
from API.Resources.RegexSample import ns as nsRegExSample

import re
import uuid


app = flask.Flask(__name__)


def configure_app(flask_app):
    flask_app.config["SWAGGER_UI_JSONEDITOR"] = settings.SWAGGER_UI_JSONEDITOR
    #flask_app.config["SERVER_NAME"] = settings.SERVER_NAME

def init_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(nsHello)
    api.add_namespace(nsAudit)
    api.add_namespace(nsRunKeeper)
    api.add_namespace(nsRegExSample)
    flask_app.register_blueprint(blueprint)


def main():
    configure_app(app)
    init_app(app)
    app.run(debug=settings.USE_DEBUG, port = settings.PORT, host="0.0.0.0")



if __name__ == '__main__':
    main()
