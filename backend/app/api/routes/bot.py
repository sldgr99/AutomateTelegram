from flask_restful import Resource


class Bot(Resource):
    def get(self):
        return "Page for work with bot"
        