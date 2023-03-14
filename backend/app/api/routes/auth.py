from flask import request, jsonify
from functools import wraps
import jwt
from flask_restful import Resource
from ..model.User import User


# decorator for blueprint
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query\
                .filter_by(public_id=data['public_id'])\
                .first()
        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)
  
    return decorated


class LoginApi(Resource):
    def get(self):
        return "login" 

    def post(self):
        return "LoginPage"


class SignupApi(Resource):
    def get(self):
        return "signup"

    def post(self):
        return "SignUpPage"
