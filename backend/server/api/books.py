from flask import Blueprint
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
    def get(self, book_id):
        return BookRepository.get_by_id(book_id)

    def delete(self, book_id):
        return BookRepository.delete(book_id)


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

    def get(self):
        return BookRepository.get_all()

    def post(self):
        args = self.get_args()
        book_id = args.get('book_id')
        title = args.get('title')
        year = args.get('year')
        return BookRepository.create(book_id, title, year)
