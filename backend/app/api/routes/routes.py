from .auth import SignupApi, LoginApi
from .blog import HomePage, Contact, HowWorks
from .bot import Bot


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/signup')
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(HomePage, '/home')
    api.add_resource(Contact, '/contact')
    api.add_resource(HowWorks, '/how-it-works')
    api.add_resource(Bot, "/api/bot")
