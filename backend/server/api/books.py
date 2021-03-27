from flask import Blueprint, jsonify, session
from flask_restful import Api, Resource, reqparse
from server.repositories import BookRepository
from . import token_required

api_books_bp = Blueprint('api_books_bp', __name__)
api = Api(api_books_bp)


@api.resource('/api/books/<book_id>')
class Book(Resource):
    """
    /api/books/<book_id> endpoint
    """
    def get_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=int)
        parser.add_argument('rating', type=int)
        return parser.parse_args()

    def get(self, book_id):
        return jsonify(BookRepository.get_by_id(book_id))

    def delete(self, book_id):
        return BookRepository.delete(book_id)

    def put(self, book_id):
        email = session.get("email")
        if email is None:
            return {}
        args = self.get_args()
        return BookRepository.update(book_id, email, args)


@api.resource('/api/books', '/api/books/')
class Books(Resource):
    """
    /api/books endpoint
    """
    def get_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', type=int)
        parser.add_argument('title', type=str)
        parser.add_argument('year', type=str)
        return parser.parse_args()

    @staticmethod
    def get_criterion() -> bool:
        parser = reqparse.RequestParser()
        parser.add_argument('get_all', type=bool)
        get_all = parser.parse_args().get("get_all")
        return get_all

    def get(self):
        if not self.get_criterion():
            email = session.get("email")
            return BookRepository.get_all(email)
        return BookRepository.get_all()

    def post(self):
        args = self.get_args()
        book_id = args.get('book_id')
        title = args.get('title')
        year = args.get('year')
        return BookRepository.create(book_id, title, year)
