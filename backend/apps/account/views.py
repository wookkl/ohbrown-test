from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from apps.account import serializers, dto, services
from utils.viewset import CustomViewSet


class UserViewSet(CustomViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'], detail=False, url_path='mine')
    def mine(self, request):
        data = serializers.UserResponseSerializer(request.user).data
        return self.response(status=status.HTTP_200_OK, data=data)


class AuthViewSet(CustomViewSet):
    @action(methods=['POST'], detail=False, url_path='sign-up')
    def sign_up(self, request):
        serializer = serializers.AuthSignUpRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = dto.AuthSignUpCommand.to_command(serializer.validated_data)
        token = services.auth_sign_up(command=cmd)
        data = serializers.JWTTokenResponseSerializer(token).data
        return self.response(status=status.HTTP_201_CREATED, data=data)
