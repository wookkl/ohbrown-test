from rest_framework.serializers import Serializer


def create_serializer_class(name, fields):
    return type(name, (Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name="inline_serializer", fields=fields)
    if data is not None:
        return serializer_class(data=data, **kwargs)
    return serializer_class(**kwargs)
