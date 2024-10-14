from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from planetarium.models import ShowTheme
from planetarium.serializers import ShowThemeSerializer


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
