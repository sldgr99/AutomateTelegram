from ...db import db
from .Subscription import Subscription


class User(db.Document):
    username = db.StringField(required=True)
    name = db.StringField(required=True)
    email = db.EmailField()
    password = db.StringField(required=True)
    premium = db.ReferenceField(Subscription)
    