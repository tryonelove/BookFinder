import datetime

import jwt
from flask import Blueprint, session, current_app
from flask_restful import Api, Resource, reqparse
from server.models import User
from server.repositories import UserRepository, UserInfoRepository

auth_bp = Blueprint('auth', __name__)

api = Api(auth_bp)

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)
parser.add_argument('first_name', type=str)
parser.add_argument('last_name', type=str)


class Register(Resource):
    """
    /api/register endpoint
    """
    def post(self):
        args = parser.parse_args()
        first_name = args['first_name']
        last_name = args['last_name']
        email = args['email']
        password = args['password']
        user = UserRepository.create(email=email,
                                     password=password)
        user = UserInfoRepository.create(user_id=user.user_id,
                                         first_name=first_name,
                                         last_name=last_name)

        return user.to_dict(), 201


class Login(Resource):
    """
    /api/login endpoint
    """
    def post(self):
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        user = User.authenticate(email=email, password=password)

        if not user:
            return {
                    'message': 'Invalid credentials',
                    'authenticated': False
                }, 401
        token = jwt.encode({
            'sub': user.email,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            },
            current_app.secret_key,
            algorithm="HS256")

        return {'token': token}


class Logout(Resource):
    """
    /api/logout endpoint
    """
    def post(self):
        if session.get("email") is not None:
            session['logged_in'] = False
        return {'status': 'ok'}, 200


api.add_resource(Register, '/api/auth/register')
api.add_resource(Login, '/api/auth/login')
api.add_resource(Logout, '/api/auth/logout')
