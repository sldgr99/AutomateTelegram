from flask_mongoengine import MongoEngine

db = MongoEngine()


def get_db():
    return db


def initialize_db(app):
    db.init_app(app)
