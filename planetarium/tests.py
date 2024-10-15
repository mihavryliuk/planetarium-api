from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from planetarium.models import ShowTheme, PlanetariumDome, AstronomyShow
from planetarium.serializers import (
    ShowThemeSerializer,
    PlanetariumDomeSerializer,
    AstronomyShowListSerializer
)

SHOW_THEME_URL = reverse("planetarium:showtheme-list")
PLANETARIUM_DOME_URL = reverse("planetarium:planetariumdome-list")
ASTRONOMY_SHOW_URL = reverse("planetarium:astronomyshow-list")


def sample_show_theme(name="Sample Theme"):
    return ShowTheme.objects.create(name=name)


def sample_planetarium_dome(name="Main Dome", rows=10, seats_in_row=15):
    return PlanetariumDome.objects.create(
        name=name,
        rows=rows,
        seats_in_row=seats_in_row
    )


def sample_astronomy_show(
        title="Sample Show",
        description="Sample Description",
        duration=60
):
    return AstronomyShow.objects.create(
        title=title,
        description=description,
        duration=duration
    )


class UnauthenticatedShowThemeApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        response = self.client.get(SHOW_THEME_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedShowThemeApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@test.com",
            password="password123",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_list_show_themes(self):
        sample_show_theme()
        sample_show_theme(name="Another Theme")

        response = self.client.get(SHOW_THEME_URL)
        show_themes = ShowTheme.objects.all()
        serializer = ShowThemeSerializer(show_themes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sorted(response.data, key=lambda x: x['id']),
                         sorted(serializer.data, key=lambda x: x['id']))

    def test_create_show_theme(self):
        payload = {"name": "New Theme"}
        response = self.client.post(SHOW_THEME_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ShowTheme.objects.filter(
            name=payload["name"]).exists()
        )


class PlanetariumDomeApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@test.com",
            password="password123",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_list_planetarium_domes(self):
        """Test retrieving a list of planetarium domes."""
        sample_planetarium_dome()
        sample_planetarium_dome(name="Secondary Dome", rows=5, seats_in_row=20)

        response = self.client.get(PLANETARIUM_DOME_URL)
        domes = PlanetariumDome.objects.all()
        serializer = PlanetariumDomeSerializer(domes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_planetarium_dome(self):
        payload = {"name": "Test Dome", "rows": 8, "seats_in_row": 12}
        response = self.client.post(PLANETARIUM_DOME_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(PlanetariumDome.objects.filter(
            name=payload["name"]).exists()
        )


class AstronomyShowApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@test.com",
            password="password123",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_list_astronomy_shows(self):
        sample_astronomy_show()
        sample_astronomy_show(title="Another Show")

        response = self.client.get(ASTRONOMY_SHOW_URL)
        shows = AstronomyShow.objects.all()
        serializer = AstronomyShowListSerializer(shows, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sorted(response.data, key=lambda x: x['id']),
                         sorted(serializer.data, key=lambda x: x['id']))

    def test_create_astronomy_show(self):
        payload = {
            "title": "New Show",
            "description": "New show description",
            "duration": 60
        }
        response = self.client.post(ASTRONOMY_SHOW_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            AstronomyShow.objects.filter(title=payload["title"]).exists()
        )
