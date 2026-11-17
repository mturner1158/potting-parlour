from django.test import TestCase
from django.urls import reverse

from plants.models import Category, Plant


class BasketTests(TestCase):
    def setUp(self):
        """Set up a plant"""
        category = Category.objects.create(name="Tropical", slug="tropical")
        self.plant = Plant.objects.create(
            category=category, name="Monstera", slug="monstera", price="10.00"
        )

    def test_add_to_basket(self):
        """Add a plant to the basket"""
        self.client.post(
            reverse("add_to_basket", args=[self.plant.id]),
            {"quantity": 2, "redirect_url": "/"},
        )
        self.assertEqual(self.client.session["basket"], {str(self.plant.id): 2})

    def test_remove_from_basket(self):
        """Remove a plant from the basket"""
        self.client.post(
            reverse("add_to_basket", args=[self.plant.id]),
            {"quantity": 2, "redirect_url": "/"},
        )
        self.client.post(reverse("remove_from_basket", args=[self.plant.id]))
        self.assertEqual(self.client.session["basket"], {})

    def test_basket_total_is_correct(self):
        """Sum of plant prices is correct"""
        self.client.post(
            reverse("add_to_basket", args=[self.plant.id]),
            {"quantity": 2, "redirect_url": "/"},
        )
        response = self.client.get(reverse("view_basket"))
        self.assertEqual(float(response.context["total"]), 20.00)

    def test_add_to_basket_rejects_get(self):
        """Basket does not change when someone visits URL"""
        response = self.client.get(reverse("add_to_basket", args=[self.plant.id]))
        self.assertEqual(response.status_code, 405)
