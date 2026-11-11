from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse

from basket.contexts import basket_contents
from profiles.models import Profile

from .forms import OrderForm
from .models import Order, OrderLineItem

import json
import stripe

from .forms import OrderForm

def checkout(request):
    current_basket = basket_contents(request)

    if not current_basket["basket_items"]:
        messages.error(request, "There is nothing in your basket")
        return redirect("all_plants")

    if not settings.STRIPE_SECRET_KEY:
        raise ValueError("Stripe secret key has not been configured")

    client = stripe.StripeClient(settings.STRIPE_SECRET_KEY)
    stripe_total = int(round(current_basket["grand_total"] * 100))
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        client_secret = request.POST.get("client_secret", "")
        pid = client_secret.split("_secret")[0]

        if order_form.is_valid() and pid:
            # checks if payment is already made for the order
            existing = Order.objects.filter(stripe_pid=pid).first()
            if existing:
                return redirect("checkout_success", order_number=existing.order_number)

            # checks if payment went through
            intent = client.v1.payment_intents.retrieve(pid)
            if intent.status == "succeeded" and intent.amount == stripe_total:
                order = order_form.save(commit=False)
                order.stripe_pid = pid
                order.original_basket = json.dumps(request.session.get("basket", {}))

                if request.user.is_authenticated:
                    profile, _ = Profile.objects.get_or_create(user=request.user)
                    order.user_profile = profile
                order.save()

                for item in current_basket["basket_items"]:
                    OrderLineItem.objects.create(
                        order=order, plant=item["plant"], quantity=item["quantity"]
                    )

                request.session["save_info"] = "save-info" in request.POST
                return redirect("checkout_success", order_number=order.order_number)

            messages.error(request, "We couldn't confirm your payment. Please try again.")
        else:
            messages.error(
                request,
                "There was an error with your form. Please double check your information.",
            )
    else:
        initial = {}
        if request.user.is_authenticated:
            profile, _ = Profile.objects.get_or_create(user=request.user)
            initial = {
                "full_name": request.user.get_full_name(),
                "email": request.user.email,
                "phone_number": profile.default_phone,
                "street_address1": profile.default_street_address1,
                "street_address2": profile.default_street_address2,
                "town_or_city": profile.default_town_or_city,
                "postcode": profile.default_postcode,
                "country": profile.default_country,
            }
            # Skip empty values so they don't override the form's own defaults
            initial = {key: value for key, value in initial.items() if value}

        order_form = OrderForm(initial=initial)

    # create the intent
    intent = client.v1.payment_intents.create(
        params={
            "amount": stripe_total,
            "currency": settings.STRIPE_CURRENCY,
            "automatic_payment_methods": {"enabled": True, "allow_redirects": "never"},
        }
    )

    template = 'checkout/checkout.html'

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated and request.session.get("save_info"):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.default_phone = order.phone_number
        profile.default_street_address1 = order.street_address1
        profile.default_street_address2 = order.street_address2
        profile.default_town_or_city = order.town_or_city
        profile.default_postcode = order.postcode
        profile.default_country = order.country
        profile.save()

    messages.success(request, f"Order placed! Your order number is {order.order_number}.")

    for key in ("basket", "save_info"):
        request.session.pop(key, None)

    template = 'checkout/checkout_success.html'

    context = {
        "order": order
        }

    return render(request, template, context)
