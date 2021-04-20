import datetime

import jwt
from flask import Blueprint, current_app
from flask_restful import Api, Resource, reqparse
from server.models import User
from server.repositories import UserRepository, UserInfoRepository
from werkzeug.security import generate_password_hash


auth_bp = Blueprint('auth_bp', __name__)

api = Api(auth_bp)


@api.resource('/api/auth/register')
class Register(Resource):
    """
    /api/аuth/register endpoint
    """

    def get_args(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        args = parser.parse_args()
        return args

    def post(self):
        args = self.get_args()
        first_name = args.get('first_name')
        last_name = args.get('last_name')
        email = args.get('email')
        password = args.get('password')
        user = UserRepository.create(email=email,
                                     password=password)
        if not user:
            return {
                'message': 'Email already exists',
            }, 401
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
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        return args

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
        
        user_info = UserInfoRepository.get(user_id=user.user_id)
        token = jwt.encode({
            'id': user.user_id,
            'name': user_info.get("first_name"),
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
            current_app.secret_key,
            algorithm="HS256")

        return {'token': token }, 200
