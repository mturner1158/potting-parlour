from django.test import TestCase
from django.urls import reverse


class CoreTests(TestCase):
    def test_home_page_loads(self):
        """The home page loads"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
