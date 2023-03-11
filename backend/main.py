from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "<p>Main!</p>"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
