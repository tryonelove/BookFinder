from . import BaseModel, db


class Author(BaseModel, db.Model):
    __tablename__ = "authors"

    author_id = db.Column(db.Integer,
                          primary_key=True,
                          unique=True,
                          nullable=False)
    author_name = db.Column(db.String())

    def __init(self, author_id: int, author_name: str):
        self.author_id = author_id
        self.author_name = author_name


class AuthorBook(BaseModel, db.Model):
    __tablename__ = "authors_books"

    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        primary_key=True, unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))

    def __init(self, book_id: int, author_id: int):
        self.book_id = book_id
        self.author_id = author_id
