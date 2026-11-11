import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .webhook_handler import StripeWH_Handler


@csrf_exempt
@require_POST
def webhook(request):
    """Listen for webhooks from Stripe"""
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    client = stripe.StripeClient(settings.STRIPE_SECRET_KEY)

    try:
        event = client.construct_event(payload, sig_header, settings.STRIPE_WH_SECRET)
    except Exception:
        # Bad payload or failed signature check: reject it
        return HttpResponse(status=400)

    handler = StripeWH_Handler(request)
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_payment_failed,
    }
    event_handler = event_map.get(event.type, handler.handle_event)
    return event_handler(event)
