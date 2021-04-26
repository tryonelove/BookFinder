from sqlalchemy.exc import IntegrityError
from server.models.user import User, UserGenre, UserBook, UserInfo, UserRecommendations
from server.models.book import Book, BooksGenres


class UserRepository:
    @staticmethod
    def create(email: str,
               password: str) -> dict:
        """ Create a user """
        try:
            user = User(email=email, password=password)
            user.save()
            user.flush()
        except IntegrityError:
            User.rollback()
            return None
        return user

    @staticmethod
    def get_by_email(email: str) -> User:
        """ Query a user by email and password"""
        user: dict = {}
        user = User.query.filter_by(email=email).first()
        return user


class UserInfoRepository:
    @staticmethod
    def create(user_id: int, first_name: str, last_name: str) -> dict:
        """ Create a user info entry """
        try:
            user = UserInfo(user_id=user_id,
                            first_name=first_name,
                            last_name=last_name)
            user.save()
            user.flush()
        except IntegrityError:
            User.rollback()
            return None
        return user


class UserGenreRepository:
    @staticmethod
    def create(user_id: int, genre_id: int) -> dict:
        """
        Add user's favorite genre
        """
        try:
            user_genres = UserGenre(user_id=user_id, genre_id=genre_id)
            user_genres.save()
            user_genres.flush()
        except IntegrityError:
            UserGenre.rollback()
            return None
        return user_genres.to_dict()


class UserBookRepository:
    @staticmethod
    def get(user_id: int):
        books = []
        user_books = UserBook.query.filter_by(user_id=user_id)
        if user_books is not None:
            books = [book.to_dict() for book in user_books]
        return books

    @staticmethod
    def update(user_id: int, book_id: int, rating: int, status: int) -> dict:
        user_book = UserBook.query.filter_by(
            book_id=book_id, user_id=user_id).first()
        if user_book is None:
            user_book = UserBook(
                user_id=user_id, book_id=book_id, rating=rating, status=status)
        else:
            user_book.rating = rating
            user_book.status = status
        user_book.save()
        return user_book.to_dict()


class UserRecommendationsRepository:
    @staticmethod
    def get(user_id: int):
        recommendations = {
            "user_id": user_id,
            "books": []
        }
        
        recs = UserRecommendations.query.join(Book, UserRecommendations.book_id == Book.book_id).add_columns(UserRecommendations.user_id, UserRecommendations.book_id, Book.title).filter(UserRecommendations.user_id == user_id)
        first_rec = recs.first()
        if first_rec is None:
            recs = UserGenre.query.join(BooksGenres, UserGenre.genre_id == BooksGenres.genre_id) \
                    .distinct() \
                    .join(Book, BooksGenres.book_id == Book.book_id) \
                    .add_columns(Book.book_id, Book.title) \
                    .limit(7)
        for book in recs:
            recommendations["books"].append(
                {
                    "book_id": book.book_id,
                    "title": book.title
                }
            )

        return recommendations
