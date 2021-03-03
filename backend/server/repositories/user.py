from sqlalchemy.exc import IntegrityError
from server.models.user import User, UserInfo


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
            raise Exception('User already exists')

        return user

    @staticmethod
    def get_by_email(email: str) -> User:
        """ Query a user by email and password"""
        user: dict = {}
        user = User.query.filter_by(email=email).first()
        if user is None:
            return None
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
            raise Exception('user already exists')

        return user
