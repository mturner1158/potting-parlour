from datetime import date, timedelta

from django.db import models
from django.conf import settings

from checkout.models import Order
from plants.models import Plant


class UserPlant(models.Model):
    """Plants bought by a user"""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_plants")
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT, related_name="owners")
    bought_plant = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="tracked_plants")
    nickname = models.CharField(max_length=100, blank=True)
    last_watered = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-last_watered"]

    @property
    def purchased_at(self):
        """Date the plant was ordered on"""
        return self.bought_plant.order_date.date()

    @property
    def display_name(self):
        """Returns the nickname given and the plant name if not"""
        return self.nickname or self.plant.name

    @property
    def next_watering(self):
        """Calculates when a plant next needs to be watered"""
        base = self.last_watered or self.purchased_at
        return base + timedelta(days=self.plant.watering_interval_days)

    @property
    def needs_water(self):
        return date.today() >= self.next_watering

    def mark_watered(self):
        now = date.today()
        self.last_watered = now
        self.save(update_fields=["last_watered"])
        WateringLog.objects.create(user_plant=self, watered_at=now)

    def __str__(self):
        return f"{self.display_name} ({self.owner})"


class WateringLog(models.Model):
    user_plant = models.ForeignKey(
        UserPlant, on_delete=models.CASCADE, related_name="watering_logs"
    )
    watered_at = models.DateField(default=date.today)

    class Meta:
        ordering = ["-watered_at"]
