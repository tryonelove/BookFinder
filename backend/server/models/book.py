from . import BaseModel, db


class Book(BaseModel, db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.Integer,
                        primary_key=True,
                        unique=True,
                        nullable=False)
    title = db.Column(db.String())
    rating = db.Column(db.Float)
    year = db.Column(db.String())

    def __init(self, book_id: int, title: str, year: str):
        self.title = title
        self.title = title
        self.year = year

    def to_dict(self):
        return dict(book_id=self.book_id,
                    title=self.title,
                    year=self.year)
