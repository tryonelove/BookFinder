from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server.app import create_app
from server.models import db, Book, User, UserBook, UserInfo, Author, AuthorBook , UserGenre, UserRecommendations, Genre

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Book=Book,
                User=User,
                UserBook=UserBook,
                UserInfo=UserInfo,
                UserGenre=UserGenre,
                UserRecommendations=UserRecommendations,
                Genre=Genre,
                Author=Author,
                AuthorBook=AuthorBook)

if __name__ == '__main__':
    manager.run()