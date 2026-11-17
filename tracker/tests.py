from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from checkout.models import Order, OrderLineItem
from plants.models import Category, Plant
from .models import UserPlant
from .services import add_order_to_tracker


class TrackerTests(TestCase):
    def setUp(self):
        """Create a user, category and plant"""
        self.user = User.objects.create_user("User1", password="pass12345")
        self.other = User.objects.create_user("User2", password="pass12345")
        category = Category.objects.create(name="Tropical", slug="tropical")
        self.plant = Plant.objects.create(
            category=category, name="Monstera", slug="monstera", price=Decimal("10.00")
        )

    def make_order(self, user, quantity):
        """Create an order"""
        order = Order.objects.create(
            user_profile=user.profile if user else None,
            full_name="Test",
            email="t@example.com",
            phone_number="01234",
            country="GB",
            town_or_city="York",
            street_address1="1 High Street",
        )
        OrderLineItem.objects.create(order=order, plant=self.plant, quantity=quantity)
        return order

    def test_one_tracker_entry_per_unit_bought(self):
        """
        Tracker creates one entry per product
        even when a user purchases multiple of the same
        """
        add_order_to_tracker(self.make_order(self.user, 3))
        self.assertEqual(UserPlant.objects.filter(owner=self.user).count(), 3)

    def test_guest_order_adds_nothing(self):
        """Guest users do not add to a tracker"""
        add_order_to_tracker(self.make_order(None, 2))
        self.assertEqual(UserPlant.objects.count(), 0)

    def test_dashboard_needs_login(self):
        """Users need to log in to view dashboard"""
        response = self.client.get(reverse("view_tracker"))
        self.assertNotEqual(response.status_code, 200)

    def test_other_user_cannot_see_my_plant(self):
        """Users can only see their own plants in the tracker"""
        add_order_to_tracker(self.make_order(self.user, 1))
        user_plant = UserPlant.objects.get(owner=self.user)
        self.client.login(username="User2", password="pass12345")
        response = self.client.get(reverse("tracker_details", args=[user_plant.id]))
        self.assertEqual(response.status_code, 404)

    def test_water_now_updates_last_watered(self):
        """Checks water now button updates last watered"""
        add_order_to_tracker(self.make_order(self.user, 1))
        user_plant = UserPlant.objects.get(owner=self.user)
        self.client.login(username="User1", password="pass12345")
        self.client.post(reverse("water_plant", args=[user_plant.id]))
        user_plant.refresh_from_db()
        self.assertEqual(user_plant.last_watered, date.today())
