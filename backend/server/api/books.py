from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from server.repositories import BookRepository
from . import token_required

api_books_bp = Blueprint('api_books_bp', __name__)

parser = reqparse.RequestParser()
parser.add_argument('book_id', type=int)
parser.add_argument('title', type=str)
parser.add_argument('year', type=str)

api = Api(api_books_bp)


class Book(Resource):
    """
    /api/books/<book_id> endpoint
    """
    def get(self, book_id):
        books = BookRepository.get_by_id(book_id)
        return books, 200

    def delete(self, book_id):
        books = BookRepository.delete(book_id)
        return books, 204


class Books(Resource):
    """
    /api/books endpoint
    """
    def get(self):
        books = BookRepository.get_all()
        return books

    @token_required
    def post(self, user):
        args = parser.parse_args()
        book_id = args['book_id']
        title = args['title']
        year = args['year']
        return BookRepository.create(book_id, title, year)


api.add_resource(Books, '/api/books')
api.add_resource(Book, '/api/books/<book_id>')
