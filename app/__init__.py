from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.measurement_routes import measurement_bp
    app.register_blueprint(measurement_bp, url_prefix="/api")

    return app