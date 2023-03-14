from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS

from bson import json_util, ObjectId
from datetime import datetime

from .api.routes.auth import auth


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():

    app = Flask(__name__)
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    # here register blueprint
    app.register_blueprint(auth)

    @app.route("/")
    def index():
        return "<p>Main!</p>"

    return app
