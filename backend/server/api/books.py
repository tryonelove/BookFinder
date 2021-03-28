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
        return book

    def delete(self, book_id):
        return BookRepository.delete(book_id)

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
        return book


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

    def get(self):
        books = BookRepository.get_all()
        return books

    def post(self):
        args = self.get_args()
        book_id = args.get('book_id')
        title = args.get('title')
        year = args.get('year')
        book = BookRepository.create(book_id, title, year)
        if book is None:
            return {
                'message': "Book was not created"
            }, 401
        return book
