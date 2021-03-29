from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from server.repositories import UserBookRepository

user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)


@api.resource('/api/user/books')
class UserBooks(Resource):
    """
    /api/user/books endpoint
    """

    def get_user_id(self) -> int:
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        user_id = parser.parse_args().get("user_id")
        return user_id

    def get_status_rating(self) -> dict:
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('book_id', type=int, required=True)
        parser.add_argument('status', type=int, required=True)
        parser.add_argument('rating', type=int, required=True)
        return parser.parse_args()

    def get(self):
        user_id = self.get_user_id()
        user = UserBookRepository.get(user_id)
        return user, 200

    def post(self):
        args = self.get_status_rating()
        user_id = args.get('user_id')
        book_id = args.get('book_id')
        status = args.get('status')
        rating = args.get('rating')
        user_book = UserBookRepository.update(
            user_id=user_id, book_id=book_id, status=status, rating=rating)
        return user_book, 200
