from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from server.repositories import GenreRepository, UserGenreRepository

registration_bp = Blueprint('registration_bp', __name__)
api = Api(registration_bp)


@api.resource('/api/registration/genres')
class Genres(Resource):
    """
    /api/registration/genres endpoint
    """

    def get_user_genre(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('genre_id', type=int, required=True)
        return parser.parse_args()

    def get_page(self) -> int:
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True)
        page = parser.parse_args().get("page")
        return page

    def get(self):
        page = self.get_page()
        genre = GenreRepository.get(page=page)
        if genre is None:
            return {
                'message': "Couldn't get genre page"
            }, 401
        return genre

    def post(self):
        user_genre_ids = self.get_user_genre()
        user_id = user_genre_ids.get('user_id')
        genre_id = user_genre_ids.get('genre_id')
        user_genre = UserGenreRepository.create(user_id, genre_id)
        if user_genre is None:
            return {
                'message': "Couldn't add genre to user"
            }, 401
        return user_genre
