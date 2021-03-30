from sqlalchemy.exc import IntegrityError
from server.models import Genre, BooksGenres, AuthorBook, UserGenre


class GenreRepository:
    @staticmethod
    def create(genre_id: int, genre_description: str) -> dict:
        """
        Create a genre
        """
        try:
            genre = Genre(genre_id=genre_id,
                          genre_description=genre_description)
            genre.save()
        except IntegrityError:
            genre.rollback()

        return genre.to_dict()

    @staticmethod
    def add_user_genre(user_id: int, genre_id: int) -> dict:
        """
        Add user's favorite genre
        """
        try:
            user_genre = UserGenre(user_id=user_id, genre_id=genre_id)
            user_genre.save()
        except IntegrityError:
            user_genre.rollback()

        return user_genre.to_dict()

    @staticmethod
    def get(page: int, genres_per_page: int = 9) -> dict:
        """
        Query a page of genres

        Returns json representation genres 
        """
        genres = Genre.query.paginate(page, genres_per_page, False)
        if genres is None:
            return None
        return [genre.to_dict() for genre in genres.items]
