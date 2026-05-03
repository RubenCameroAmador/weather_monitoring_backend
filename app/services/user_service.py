from app.extensions import db
from app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_user(data):
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    user = User(
        username=data["username"],
        password=hashed_password
    )       

    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_all_users():
    return User.query.all()