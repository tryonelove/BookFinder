from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def flush():
        db.session.flush()

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def commit():
        db.session.commit()
