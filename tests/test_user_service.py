from app.services.user_service import create_user, get_user_by_username, get_all_users

def test_create_user_service(app):
    data = {
        "username": "testuser",
        "password": "testpassword"
    }

    user = create_user(data)

    assert user.id is not None
    assert user.username == "testuser"
    assert user.password != "testpassword"  # Should be hashed

def test_get_user_by_username_service(app):
    data = {
        "username": "testuser2",
        "password": "testpassword2"
    }

    create_user(data)

    user = get_user_by_username("testuser2")

    assert user is not None
    assert user.username == "testuser2"

def test_get_all_users_service(app):
    data1 = {
        "username": "user1",
        "password": "pass1"
    }

    data2 = {
        "username": "user2",
        "password": "pass2"
    }

    create_user(data1)
    create_user(data2)

    users = get_all_users()

    assert len(users) >= 2
    usernames = [u.username for u in users]
    assert "user1" in usernames
    assert "user2" in usernames