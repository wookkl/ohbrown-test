import functools

from django.core import exceptions as django_exceptions
from django.db import transaction
from rest_framework.exceptions import ValidationError


def handle_exception(e):
    if isinstance(e, django_exceptions.ValidationError):
        raise ValidationError(e.messages)
    raise e


def service(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            with transaction.atomic():
                return func(*args, **kwargs)
        except Exception as e:
            handle_exception(e)
    return wrapper
