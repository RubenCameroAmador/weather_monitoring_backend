from flask import Flask
from .config import Config
from .extensions import db, migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    bcrypt = Bcrypt(app)

    if not app.config.get("JWT_SECRET_KEY"):
        app.config["JWT_SECRET_KEY"] = os.getenv("TOKEN_JWT", "dev-secret-key")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    jwt = JWTManager(app)

    from .routes.measurement_routes import measurement_bp
    app.register_blueprint(measurement_bp, url_prefix="/api")

    from .routes.user_route import user_bp
    app.register_blueprint(user_bp, url_prefix="/api")

    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api")

    return app