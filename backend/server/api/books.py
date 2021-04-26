from flask import Blueprint, jsonify, session
from flask_restful import Api, Resource, reqparse
from server.repositories import BookRepository

from . import token_required


api_books_bp = Blueprint('api_books_bp', __name__)
api = Api(api_books_bp)


@api.resource('/api/books/<int:book_id>')
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
        book = BookRepository.get_by_id(book_id)
        if book is None:
            return {
                'message': 'Book was not found',
            }, 401
        return book, 200

    def delete(self, book_id):
        book = BookRepository.delete(book_id)
        return book, 200

    def put(self, book_id):
        email = session.get("email")
        if email is None:
            return {
                'message': 'Invalid credentials',
                'authenticated': False
            }, 401
        args = self.get_args()
        book = BookRepository.update(book_id, args)
        if book is None:
            return {
                'message': "Book was not updated"
            }, 401
        return book, 200


@api.resource('/api/books')
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

    def get_page(self) -> int:
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        page = parser.parse_args().get("page")
        return page

    def get(self):
        page = self.get_page()
        books = BookRepository.get_page(page=page)
        return books, 200

    def post(self):
        args = self.get_args()
        book_id = args.get('book_id')
        title = args.get('title')
        year = args.get('year')
        book = BookRepository.create(book_id, title, year)
        if book is None:
            return {
                'message': "Book was not created"
            }, 409
        return book, 200
