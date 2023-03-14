from flask_restful import Resource

class HomePage(Resource):
    def get(self):
        return "Home"
    

class Contact(Resource):
    def get(self):
        return "Contact"


class HowWorks(Resource):
    def get(self):
        return "How it works"
