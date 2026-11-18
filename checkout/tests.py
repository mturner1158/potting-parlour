from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

import itertools
import json
from types import SimpleNamespace
from unittest.mock import patch, MagicMock

from .models import Order
from .webhook_handler import StripeWH_Handler
from plants.models import Plant, Category


# gives stripe_pids to orders
_pid_counter = itertools.count(1)


def make_order(user_profile=None, stripe_pid=None):
    """Create an order"""
    return Order.objects.create(
        user_profile=user_profile,
        stripe_pid=stripe_pid or f"pi_test_{next(_pid_counter)}",
        full_name="Test Person",
        email="test@example.com",
        phone_number="01234",
        country="GB",
        town_or_city="York",
        street_address1="1 High Street",
    )


class AnyAmount:
    """Any number"""
    def __eq__(self, other):
        return True


def fake_intent(status="succeeded"):
    """A fake Stripe payment intent."""
    intent = MagicMock()
    intent.status = status
    intent.amount = AnyAmount()
    return intent


def fake_event(pid, metadata=None):
    """A fake Stripe webhook event."""
    return SimpleNamespace(
        type="payment_intent.succeeded",
        data=SimpleNamespace(
            object=SimpleNamespace(id=pid, metadata=metadata or {})
        ),
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


class CheckoutViewPaymentTests(TestCase):
    def setUp(self):
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
        session = self.client.session
        session["basket"] = {str(self.plant.pk): 1}
        session.save()
        self.url = reverse("checkout")
        self.data = {
            "full_name": "Test Person",
            "email": "test@example.com",
            "phone_number": "01234",
            "country": "GB",
            "town_or_city": "York",
            "postcode": "YO306FG",
            "street_address1": "1 High Street",
            "client_secret": "pi_view_1_secret_abc",
        }

        # replicating a stripe payment
        patcher = patch("checkout.views.stripe.StripeClient")
        fake_stripe = patcher.start().return_value
        self.addCleanup(patcher.stop)
        fake_stripe.v1.payment_intents.create.return_value.client_secret = (
            "pi_view_1_secret_abc")
        self.stripe_retrieve = fake_stripe.v1.payment_intents.retrieve
        self.stripe_retrieve.return_value = fake_intent()


    def test_successful_payment_creates_one_order(self):
        """Successful payment and create order"""
        self.client.post(self.url, self.data)
        self.assertEqual(
            Order.objects.filter(stripe_pid="pi_view_1").count(), 1)

    def test_declined_payment_creates_no_order(self):
        """Unsuccessful payment and no order is created"""
        self.stripe_retrieve.return_value = fake_intent("requires_payment_method")
        self.client.post(self.url, self.data)
        self.assertEqual(Order.objects.count(), 0)

    def test_existing_order_redirects_without_crashing(self):
        """Order already exists so do not take payment"""
        existing = make_order(stripe_pid="pi_view_1")
        response = self.client.post(self.url, self.data)
        self.assertRedirects(
            response,
            reverse("checkout_success", args=[existing.order_number]),
            fetch_redirect_response=False)
        self.assertEqual(Order.objects.count(), 1)


class WebhookTests(TestCase):
    def setUp(self):
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
        self.handler = StripeWH_Handler(request=None)
        self.metadata = {
            "full_name": "Test Person",
            "email": "test@example.com",
            "phone_number": "01234",
            "country": "GB",
            "town_or_city": "York",
            "postcode": "YO306FG",
            "street_address1": "1 High Street",
            "basket": json.dumps({str(self.plant.pk): 2}),
            "username": "",
            "save_info": "0",
        }

    def test_existing_order_returns_200(self):
        """Order already exists so return 200"""
        make_order(stripe_pid="pi_wh_1")
        response = self.handler.handle_payment_intent_succeeded(
            fake_event("pi_wh_1"))
        self.assertEqual(response.status_code, 200)

    @patch("checkout.webhook_handler.time.sleep")
    def test_webhook_first_creates_order(self, _sleep):
        """No order exists so create a webhook"""
        response = self.handler.handle_payment_intent_succeeded(
            fake_event("pi_wh_2", self.metadata))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Order.objects.filter(stripe_pid="pi_wh_2").count(), 1)

    @patch("checkout.webhook_handler.time.sleep")
    def test_repeated_delivery_creates_one_order(self, _sleep):
        """Two identical webhooks create one order"""
        event = fake_event("pi_wh_3", self.metadata)
        self.handler.handle_payment_intent_succeeded(event)
        self.handler.handle_payment_intent_succeeded(event)
        self.assertEqual(
            Order.objects.filter(stripe_pid="pi_wh_3").count(), 1)
