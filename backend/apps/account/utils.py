from rest_framework_simplejwt.tokens import RefreshToken

from apps.account.dto import JWTTokenInfo
from apps.account.models import User


def get_token_by_user(*, user: User) -> JWTTokenInfo:
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    return JWTTokenInfo(access=str(access), refresh=str(refresh))
