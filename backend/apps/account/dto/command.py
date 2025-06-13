from dataclasses import dataclass


@dataclass
class AuthSignUpCommand:
    username: str
    first_name: str
    last_name: str
    password: str

    @staticmethod
    def to_command(validated_data):
        return AuthSignUpCommand(
            username=validated_data['username'], first_name=validated_data['first_name'],
            last_name=validated_data['last_name'], password=validated_data['password']
        )


@dataclass
class AuthLoginCommand:
    username: str
    password: str

    @staticmethod
    def to_command(validated_data):
        return AuthLoginCommand(username=validated_data['username'], password=validated_data['password'])
