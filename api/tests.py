from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Location
from api.views import LocationViewSet


class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(
            longitude="56.2397",
            latitude="58.007556",
            comment="test",
        )
        Location.objects.create(
            longitude="57.2397",
            latitude="59.007556",
            comment="test2",
        )

    def test_created_value(self):
        """
        Testing auto-set of created timestamp
        """
        locations = Location.objects.all()
        for loc in locations:
            self.assertTrue(loc.created)


class ApiTestCase(TestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.user = User.objects.create_user("test", "test@testworld.test", )
        self.passwrd = "P@$$W0Rd"
        self.user.set_password(self.passwrd)
        self.user.is_active = True
        self.user.save()

        self.view = LocationViewSet.as_view

        Location.objects.create(
            longitude="56.2397",
            latitude="58.007556",
            comment="test",
        )
        Location.objects.create(
            longitude="57.2397",
            latitude="59.007556",
            comment="test2",
        )

    def test_get_locations(self):
        token = self.get_token()
        response = self.client.get("http://testserver/api/location/", headers={
            "Authorization": f"Bearer {token}",
        })
        locations = response.json()
        for loc in locations:
            self.assertTrue(loc["created"])
            self.assertTrue(loc["longitude"])
            self.assertTrue(loc["latitude"])
            self.assertTrue(loc["comment"])

    def test_post_location(self):
        pass

    def get_token(self):
        response = self.client.post("http://testserver/api/token/", {
            "username": self.user.username, "password": self.passwrd
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.json()["access"]
