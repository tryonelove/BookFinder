import os
from flask import Flask
from api.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0", port=5000, debug=True)