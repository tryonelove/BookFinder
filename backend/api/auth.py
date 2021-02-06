from flask import Flask, Blueprint, session
from flask_restful import abort, Api, Resource, reqparse

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Login(Resource):
    """
    /api/login endpoint
    """
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        if username == 'root' and password == 'toor':
            session['logged_in'] = True
            return {'status': 'ok'}, 200
        else:
            return {'status': 'no'}, 406


class Logout(Resource):
    """
    /api/logout endpoint
    """
    def post(self):
        if session.get("username") is not None:
            session['logged_in'] = False
        return {'status': 'ok'}, 200

api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')