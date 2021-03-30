from werkzeug.security import check_password_hash, generate_password_hash
from . import BaseModel, db

class UserInfo(BaseModel, db.Model):
    __tablename__ = "users_info"

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    role = db.Column(db.Integer)

    def __init(self, user_id: int,
               first_name: str, last_name: str,
               role: int = 1):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def to_dict(self):
        return dict(user_id=self.user_id,
                    first_name=self.first_name,
                    last_name=self.last_name)


class User(BaseModel, db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(email=self.email,
                    password=self.password)


class UserBook(BaseModel, db.Model):
    __tablename__ = "users_books"

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False,
                        primary_key=True)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False,
                        primary_key=True)
    rating = db.Column(db.Integer)
    status = db.Column(db.Integer)

    __table_args__ = (
        db.UniqueConstraint("user_id", "book_id"),
    )

    def __init(self, user_id: int, book_id: int, rating: int, status: int):
        self.user_id = user_id
        self.book_id = book_id
        self.rating = rating
        self.status = status

    def to_dict(self):
        return dict(user_id=self.user_id,
                    book_id=self.book_id,
                    rating=self.rating,
                    status=self.status)


class UserGenre(BaseModel, db.Model):
    __tablename__ = "users_genres"

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False,
                        primary_key=True)
    genre_id = db.Column(db.Integer,
                        db.ForeignKey('genres.genre_id'),
                        nullable=False,
                        primary_key=True)

    def __init(self, user_id: int, genre_id: int):
        self.user_id = user_id
        self.genre_id = genre_id

    def to_dict(self):
        return dict(user_id=self.user_id,
                    genre_id=self.genre_id)


class UserRecommendations(BaseModel, db.Model):
    __tablename__ = "users_recommendations"

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False,
                        primary_key=True)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False,
                        primary_key=True)

    def __init(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id

    def to_dict(self):
        return dict(user_id=self.user_id,
                    book_id=self.book_id)