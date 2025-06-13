from dataclasses import dataclass


@dataclass
class JWTTokenInfo:
    access: str
    refresh: str
