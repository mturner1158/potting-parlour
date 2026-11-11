import json
import time

from django.http import HttpResponse

from plants.models import Plant
from profiles.models import Profile

from .forms import OrderForm
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Any event we haven't written a handler for."""
        return HttpResponse(
            content=f"Unhandled webhook received: {event.type}", status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(content=f"Webhook received: {event.type}", status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        metadata = intent.metadata

        # wait 5 seconds for order to be created
        for _ in range(5):
            if Order.objects.filter(stripe_pid=pid).exists():
                return HttpResponse(
                    content=f"Webhook received: {event.type} | SUCCESS: Order already in database",
                    status=200,
                )
            time.sleep(1)

        # build the order
        details = {field: metadata.get(field, "") for field in OrderForm.Meta.fields}
        form = OrderForm(details)
        if not form.is_valid():
            return HttpResponse(
                content=f"Webhook received: {event.type} | ERROR: {form.errors.as_json()}",
                status=500,
            )

        order = None
        try:
            basket_json = metadata.get("basket", "{}")

            order = form.save(commit=False)
            order.stripe_pid = pid
            order.original_basket = basket_json

            profile = None
            username = metadata.get("username", "")
            if username:
                profile = Profile.objects.filter(user__username=username).first()
                order.user_profile = profile
            order.save()

            for plant_id, quantity in json.loads(basket_json).items():
                OrderLineItem.objects.create(
                    order=order,
                    plant=Plant.objects.get(pk=plant_id),
                    quantity=quantity,
                )

            if profile and metadata.get("save_info") == "1":
                profile.default_phone = order.phone_number
                profile.default_street_address1 = order.street_address1
                profile.default_street_address2 = order.street_address2
                profile.default_town_or_city = order.town_or_city
                profile.default_postcode = order.postcode
                profile.default_country = order.country
                profile.save()
        except Exception as e:
            if order and order.pk:
                order.delete()
            return HttpResponse(
                content=f"Webhook received: {event.type} | ERROR: {e}", status=500
            )

        return HttpResponse(
            content=f"Webhook received: {event.type} | SUCCESS: Created order in webhook",
            status=200,
        )
