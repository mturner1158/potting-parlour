from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from checkout.models import Order


class ProfileTests(TestCase):
    def setUp(self):
        """Setup users and orders"""
        self.user_a = User.objects.create_user("User1", password="pass12345")
        self.user_b = User.objects.create_user("User2", password="pass12345")
        # The post_save signal creates the profile automatically
        self.order = Order.objects.create(
            user_profile=self.user_a.profile,
            full_name="Alice",
            email="alice@example.com",
            phone_number="01234",
            country="GB",
            town_or_city="York",
            street_address1="1 High Street",
        )

    def test_profile_profile_created_by_signal(self):
        """Profile created on account creation"""
        self.assertTrue(hasattr(self.user_a, "profile"))

    def test_profile_page_needs_login(self):
        """Users need to be logged in to see profile page"""
        response = self.client.get(reverse("view_profile"))
        self.assertNotEqual(response.status_code, 200)

    def test_owner_can_see_own_order(self):
        "Users can see their own order history"
        self.client.login(username="User1", password="pass12345")
        response = self.client.get(
            reverse("order_history", args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)

    def test_other_user_gets_404_for_order(self):
        """Users cannot see others orders"""
        self.client.login(username="User2", password="pass12345")
        response = self.client.get(reverse(
            "order_history",
            args=[self.order.order_number])
            )
        self.assertEqual(response.status_code, 404)
