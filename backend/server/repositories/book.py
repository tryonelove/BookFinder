from sqlalchemy.exc import IntegrityError
from server.models import Book, BooksGenres, AuthorBook, UserBook, User, Author
from server.models import db

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
            return None
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
            return None
        return book.to_dict()

    @staticmethod
    def get_all(user_id: int = None) -> list:
        """
        Query all books
        """
        books = []
        if user_id is None:
            books = Book.query.all()
            books = [book.to_dict() for book in books]
        return books

    @staticmethod
    def get_page(page: int = None, books_per_page: int = 12) -> dict:
        """
        Query all books
        """
        books = db.session.query(Book, AuthorBook, Author) \
                .join(AuthorBook, Book.book_id == AuthorBook.book_id) \
                .join(Author, Author.author_id == AuthorBook.author_id) \
                .paginate(page, books_per_page, False)
        if books is None:
            return None
        return [{**(book.to_dict()), **(author_book.to_dict()), **(author.to_dict())} for book, author_book, author in books.items]

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
