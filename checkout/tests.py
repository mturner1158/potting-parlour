from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Order


def make_order(user_profile=None):
    """Create an order"""
    return Order.objects.create(
        user_profile=user_profile,
        full_name="Test Person",
        email="test@example.com",
        phone_number="01234",
        country="GB",
        town_or_city="York",
        street_address1="1 High Street",
    )


class CheckoutSuccessTests(TestCase):
    def test_guest_who_just_ordered_can_see_success_page(self):
        """Successful order shows success page"""
        order = make_order()
        session = self.client.session
        session["last_order_number"] = order.order_number
        session.save()
        response = self.client.get(reverse(
            "checkout_success",
            args=[order.order_number])
            )
        self.assertEqual(response.status_code, 200)

    def test_unath_gets_404(self):
        """Unauthenticated user cannot see previous orders"""
        order = make_order()
        response = self.client.get(reverse(
            "checkout_success",
            args=[order.order_number])
            )
        self.assertEqual(response.status_code, 404)

    def test_other_signed_in_user_gets_404(self):
        """Users can only see their own order"""
        owner = User.objects.create_user("User1", password="pass12345")
        User.objects.create_user("User2", password="pass12345")
        order = make_order(owner.profile)
        self.client.login(username="User2", password="pass12345")
        response = self.client.get(reverse(
            "checkout_success",
            args=[order.order_number])
            )
        self.assertEqual(response.status_code, 404)

    def test_owner_can_see_success_page(self):
        """A user can see their own orders"""
        owner = User.objects.create_user("User1", password="pass12345")
        order = make_order(owner.profile)
        self.client.login(username="User1", password="pass12345")
        response = self.client.get(reverse(
            "checkout_success",
            args=[order.order_number])
            )
        self.assertEqual(response.status_code, 200)
