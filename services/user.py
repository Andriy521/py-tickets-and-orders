from db.models import User
from typing import Optional


def create_user(username: str,
                password: str,
                email: Optional[str],
                first_name: Optional[str],
                last_name: Optional[str],
                ) -> User:
    user = User.objects.create_user(username=username, password=password)

    if email:
        user.email = email

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    user.save()
    return user


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(user_id: int,
                username: str = None,
                password: str = None,
                email: str = None,
                first_name: str = None,
                last_name: str = None,) -> User:
    user = User.objects.get(id=user_id)

    if username:
        user.username = username

    if password:
        user.set_password(password)

    if email:
        user.email = email

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    user.save()
    return user
