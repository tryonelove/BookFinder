import datetime

import jwt
from flask import Blueprint, session, current_app
from flask_restful import Api, Resource, reqparse
from backend.server.models import User
from backend.server.repositories import UserRepository, UserInfoRepository

auth_bp = Blueprint('auth', __name__)

api = Api(auth_bp)


@api.resource('/api/auth/register')
class Register(Resource):
    """
    /api/auth/register endpoint
    """
    def get_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        return parser.parse_args()

    def post(self):
        args = self.get_args()
        first_name = args.get('first_name')
        last_name = args.get('last_name')
        email = args.get('email')
        password = args.get('password')

        user = UserRepository.create(email=email,
                                     password=password)
        user = UserInfoRepository.create(user_id=user.user_id,
                                         first_name=first_name,
                                         last_name=last_name)

        return user.to_dict(), 201


@api.resource('/api/auth/login')
class Login(Resource):
    """
    /api/auth/login endpoint
    """
    def get_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        return parser.parse_args()

    def post(self):
        args = self.get_args()
        email = args.get('email')
        password = args.get('password')

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
