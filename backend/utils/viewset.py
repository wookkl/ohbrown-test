from rest_framework.viewsets import GenericViewSet

from utils.mixin import CustomResponseMixin


class CustomViewSet(GenericViewSet, CustomResponseMixin):
    pass
