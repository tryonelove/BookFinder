from flask import Flask
from flask_cors import CORS


def register_flask_blueprints(app: Flask):
    from server.api.auth import auth_bp
    from server.api.books import api_books_bp
    from server.api.registration import registration_bp
    from server.api.user import user_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(api_books_bp)
    app.register_blueprint(registration_bp)
    app.register_blueprint(user_bp)


def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.DevelopmentConfig')
    app.url_map.strict_slashes = False

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    register_flask_blueprints(app)

    from server.models import db
    db.init_app(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
