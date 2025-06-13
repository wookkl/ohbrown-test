from rest_framework import serializers


class AuthSignUpRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("패스워드가 일치하지 않습니다.")
        return attrs


class JWTTokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class AuthLoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=128)


class UserResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
