from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.account.views import UserViewSet, AuthViewSet

app_name = 'account'

router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='user')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path(r'', include(router.urls)),
]
