from django.http import HttpResponse


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
