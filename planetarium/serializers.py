from rest_framework import serializers

from planetarium.models import ShowTheme, PlanetariumDome, AstronomyShow


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields =("id", "name")


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "themes",
        )


class AstronomyShowListSerializer(AstronomyShowSerializer):
    themes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "themes", "image")


class AstronomyShowDetailSerializer(AstronomyShowSerializer):
    themes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = (
            "id",
            "title",
            "duration",
            "description",
            "themes",
            "image",
        )


class AstronomyShowImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "image")
