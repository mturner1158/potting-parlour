import uuid
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.db.models import Sum

from plants.models import Plant
from profiles.models import Profile


class Order(models.Model):
    """
    records shop orders
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=60, default="United Kingdom")

    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=Decimal("0.00")
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )

    # Snapshot of the session basket and the payment reference (if using Stripe)
    original_basket = models.TextField(blank=True, default="")
    stripe_pid = models.CharField(max_length=254, blank=True, default="")

    class Meta:
        ordering = ["-date"]

    def _generate_order_number(self):
        """Random, unique order number."""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Recalculate totals each time a line item is added, changed or removed."""
        self.order_total = self.lineitems.aggregate(Sum("lineitem_total"))[
            "lineitem_total__sum"
        ] or Decimal("0.00")

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total
                * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
                / 100
            ).quantize(Decimal("0.01"))
        else:
            self.delivery_cost = Decimal("0.00")

        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    def save(self, *args, **kwargs):
        """Set the order number on first save."""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    model for each item in an order
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="lineitems"
    )
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(
        max_digits=8, decimal_places=2, editable=False
    )

    def save(self, *args, **kwargs):
        """Set the line total on save."""
        self.lineitem_total = self.plant.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.plant.name} x {self.quantity} on order {self.order.order_number}"
