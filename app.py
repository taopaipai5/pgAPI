import flask
import settings
from flask import Blueprint
from API.ApiManager import api,apiv2
from API.Resources.Hello import ns as nsHello
from API.Resources.RunkeeperActivity import ns as nsRunKeeper
from API.Resources.RegexSample import ns as nsRegExSample
from API.Resources.AuditActivity import ns as nsAudit,nsv2 as nsAuditv2
from API.Resources.Scope import ns as nsScope
from Database import mongoDb

app = flask.Flask(__name__)

def configure_app(flask_app):
    flask_app.config["SWAGGER_UI_JSONEDITOR"] = settings.SWAGGER_UI_JSONEDITOR
    flask_app.config["MONGO_DBNAME"] = settings.DB_NAME
    flask_app.config["MONGO_URI"] = settings.DB_CONNECTION

def init_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(nsHello)
    api.add_namespace(nsAudit)
    api.add_namespace(nsRunKeeper)
    api.add_namespace(nsRegExSample)
    api.add_namespace(nsScope)
    flask_app.register_blueprint(blueprint)
    mongoDb.init_app(flask_app)

    blueprintv2 = Blueprint('apiv2', __name__, url_prefix='/api/v2')
    apiv2.init_app(blueprintv2)
    apiv2.add_namespace(nsAuditv2)
    flask_app.register_blueprint(blueprintv2)



def main():
    configure_app(app)
    init_app(app)
    app.run(debug=settings.USE_DEBUG, port = settings.PORT, host="0.0.0.0")



if __name__ == '__main__':
    main()
