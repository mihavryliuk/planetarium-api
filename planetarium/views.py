from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from planetarium.models import ShowTheme, PlanetariumDome
from planetarium.serializers import ShowThemeSerializer, PlanetariumDomeSerializer


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetariumDomeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer