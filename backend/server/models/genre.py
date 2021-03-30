from . import BaseModel, db


class Genre(BaseModel, db.Model):
    __tablename__ = "genres"

    genre_id = db.Column(db.Integer,
                         primary_key=True,
                         unique=True,
                         autoincrement=True)
    genre_description = db.Column(db.String(), unique=True)

    def to_dict(self):
        return dict(genre_id=self.genre_id,
                    genre_description=self.genre_description)
