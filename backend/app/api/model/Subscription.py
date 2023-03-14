from ...db import db


class Subscription(db.Document):
    type_subscription = db.StringField(required=True)
