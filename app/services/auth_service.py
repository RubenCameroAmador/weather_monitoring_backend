from app.services.user_service import get_user_by_username
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def validate_user (username, password):
    user = get_user_by_username(username)
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return None
