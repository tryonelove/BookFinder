from sqlalchemy.exc import IntegrityError
from server.models import Book


class BookRepository:
    @staticmethod
    def create(book_id: int, title: str, year: str) -> dict:
        """
        Create a book
        """
        result: dict = {}
        try:
            book = Book(book_id=book_id, title=title, year=year)
            book.save()
            result = {
                'book_id': book.book_id,
                'title': book.title,
                'year': book.year,
            }
        except IntegrityError:
            Book.rollback()
            raise Exception('Book already exists')

        return result

    @staticmethod
    def get_by_id(book_id: int) -> dict:
        """
        Query a book by book_id
        """
        book: dict = {}
        book = Book.query.filter_by(book_id=book_id).first_or_404()
        book = {
            'book_id': book.book_id,
            'title': book.title,
            'year': book.year,
        }
        return book

    @staticmethod
    def get_all() -> dict:
        """
        Query all books
        """
        books: dict = {}
        books = Book.query.all()
        return {"books": [book.to_dict() for book in books]}

    @staticmethod
    def delete(book_id: int) -> dict:
        """
        Delete book by book_id
        """
        book = Book.query.filter_by(Book.book_id == book_id).delete()
        book.save()
        return {"books": [book.to_dict()]}
