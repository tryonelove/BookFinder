from sqlalchemy.exc import IntegrityError
from server.models import Book, BooksGenres, AuthorBook, UserBook, User


class BookRepository:
    @staticmethod
    def create(book_id: int, title: str, year: str) -> dict:
        """
        Create a book
        """
        try:
            book = Book(book_id=book_id, title=title, year=year)
            book.save()
        except IntegrityError:
            Book.rollback()

        return book.to_dict()

    @staticmethod
    def get_by_id(book_id: int) -> dict:
        """
        Query a book by book_id

        Returns json representation
        of book
        """
        book = Book.query.filter_by(book_id=book_id).first()
        if book is None:
            return {}
        return book.to_dict()

    @staticmethod
    def get_all(email: str = None) -> list:
        """
        Query all books
        """
        books = []
        if email is None:
            books = Book.query.all()
            books = [book.to_dict() for book in books]
        else:
            user = User.query.filter_by(email=email).first()
            user_id = user.get("user_id", None)
            if user_id is not None:
                user_books = UserBook.query.filter_by(user_id=user_id).first()
                books = [book.to_dict() for book in user_books]
        return books

    @staticmethod
    def delete(book_id: int) -> dict:
        """
        Delete book by book_id

        Returns { "book_id" : book_id }.
        If book doesn't exist, book_id is -1.
        """
        AuthorBook.query.filter_by(book_id=book_id).delete()
        BooksGenres.query.filter_by(book_id=book_id).delete()
        book = Book.query.filter_by(book_id=book_id).delete()
        # book = 0 if it doesn't exist
        if book != 0:
            Book.commit()
        else:
            book_id = -1
        return {"book_id": int(book_id)}

    @staticmethod
    def update(book_id: int, user_email: str, args: list) -> dict:
        user = User.query.filter_by(email=user_email).first()
        if user is not None and user.get("user_id", None) is not None:
            book = UserBook.query.filter_by(book_id=book_id, user_id=user.get("user_id")).first()
            if book is not None:
                for characteristic in args:
                    setattr(book, characteristic, getattr(args, characteristic))
                book.save()
                return book.to_dict()
        return {}
