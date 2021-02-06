from flask import Flask, Blueprint
from flask_restful import abort, Api, Resource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


BOOKS = {
    "book1" : {"title": "book_title1"},
    "book2" : {"title": "book_title2"},
    "book3" : {"title": "book_title3"}
}


def abort_if_book_doesnt_exist(book_id):
    if book_id not in BOOKS:
        abort(404, message="Book {} doesn't exist".format(book_id))


class Book(Resource):
    """
    /api/books/<book_id> endpoint
    """
    def get(self, book_id):
        abort_if_book_doesnt_exist(book_id)
        return BOOKS[book_id]

    def delete(self, book_id):
        abort_if_book_doesnt_exist(book_id)
        del BOOKS[book_id]
        return '', 204


class Books(Resource):
    """
    /api/books endpoint
    """
    def get(self):
        return BOOKS

api.add_resource(Books, '/api/books')
api.add_resource(Book, '/api/books/<book_id>')
