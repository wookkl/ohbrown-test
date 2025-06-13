from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

from apps.account.dto import AuthSignUpCommand
from apps.account.models import User
from apps.account.utils import get_token_by_user
from utils.decorators import service


@service
def user_create(*, command: AuthSignUpCommand) -> User:
    is_username_dup = User.objects.filter(username=command.username).exists()
    if is_username_dup:
        raise ValidationError('아이디가 이미 있습니다.')
    user = User(
        username=command.username, first_name=command.first_name, last_name=command.last_name
    )
    validate_password(command.password)
    user.set_password(command.password)
    user.save()
    return user


@service
def auth_sign_up(*, command: AuthSignUpCommand):
    user = user_create(command=command)
    return get_token_by_user(user=user)
