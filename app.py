import flask
from flask import Blueprint

from API.ApiManager import api
from API.Resources.Hello import ns as nsHello
from API.Resources.AuditActivity import ns as nsAudit

app = flask.Flask(__name__)


def configure_app(flask_app):
    flask_app.config["SWAGGER_UI_JSONEDITOR"] = True

def init_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(nsHello)
    api.add_namespace(nsAudit)
    flask_app.register_blueprint(blueprint)

def main():
    configure_app(app)
    init_app(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()
