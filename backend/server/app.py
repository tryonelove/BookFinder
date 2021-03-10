from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.DevelopmentConfig')
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from server.api.auth import auth_bp
    from server.api.books import api_books_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_books_bp)
    
    from server.models import db
    db.init_app(app)
    
    return app


