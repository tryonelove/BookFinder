from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.DevelopmentConfig')

    from backend.server.api.auth import auth_bp
    from backend.server.api.books import api_books_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_books_bp)
    
    from backend.server.models import db
    db.init_app(app)
    
    return app


