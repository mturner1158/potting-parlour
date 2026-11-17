from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Category, Plant


class PlantTests(TestCase):
    def setUp(self):
        """Create category and plant"""
        self.category = Category.objects.create(
            name="Tropical",
            slug="tropical"
            )
        self.plant = Plant.objects.create(
            category=self.category,
            name="Monstera",
            slug="monstera",
            price="12.99",
            is_active=True,
        )
        self.hidden = Plant.objects.create(
            category=self.category,
            name="Cheese Plant",
            slug="cheese-plant",
            price="5.00",
            is_active=False,
        )

    def test_all_plants_page_loads(self):
        """All plants view loads"""
        response = self.client.get(reverse("all_plants"))
        self.assertEqual(response.status_code, 200)

    def test_inactive_plant_not_listed(self):
        """Plants marked is_active=True not shown"""
        response = self.client.get(reverse("all_plants"))
        self.assertContains(response, "Monstera")
        self.assertNotContains(response, "Hidden Plant")

    def test_plant_detail_loads(self):
        "plant detail page loads"
        response = self.client.get(
            reverse("plant_detail", args=[self.plant.slug])
            )
        self.assertEqual(response.status_code, 200)

    def test_normal_user_cannot_add_plant(self):
        """Only superusers can add plants"""
        User.objects.create_user("User1", password="pass12345")
        self.client.login(username="User1", password="pass12345")
        response = self.client.get(reverse("add_plant"))
        self.assertIn(response.status_code, [302, 403])
