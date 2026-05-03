import pytest
from app import create_app
from app.extensions import db
from flask_jwt_extended import create_access_token


@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "JWT_SECRET_KEY": "super-secret-key-for-testing-1234567890",
        "JWT_ACCESS_TOKEN_EXPIRES": 3600
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(app):
    with app.app_context():
        token = create_access_token(identity="test_user")
    return {
        "Authorization": f"Bearer {token}"
    }