from sqlalchemy.exc import IntegrityError
from server.models import Book


class BookRepository:
    @staticmethod
    def create(book_id: int, title: str, year: str) -> dict:
        """
        Create a book
        """
        books = []
        try:
            book = Book(book_id=book_id, title=title, year=year)
            book.save()
        except IntegrityError:
            return books

        books.append(book)
        return books

    @staticmethod
    def get_by_id(book_id: int) -> dict:
        """
        Query a book by book_id
        """
        books = []
        book = Book.query.filter_by(book_id=book_id).first()
        if book is None:
            return books
        books.append(book.to_dict())
        return books

    @staticmethod
    def get_all() -> dict:
        """
        Query all books
        """
        books: dict = {}
        books = Book.query.all()
        return [book.to_dict() for book in books]

    @staticmethod
    def delete(book_id: int) -> dict:
        """
        Delete book by book_id
        """
        books = []
        book = Book.query.filter_by(Book.book_id == book_id).delete()
        book.save()
        books.append(book.to_dict())
        return books
