from decimal import Decimal
from django.conf import settings

from plants.models import Plant


def basket_contents(request):
    """Basket total to be used throughout the project"""
    basket = request.session.get("basket", {})
    plants = Plant.objects.filter(pk__in=basket.keys(), is_active=True)

    basket_items = []
    total = Decimal("0.00")
    plant_count = 0

    for plant in plants:
        quantity = basket[str(plant.pk)]
        subtotal = plant.price * quantity
        total += subtotal
        plant_count += quantity
        basket_items.append(
            {"plant": plant, "quantity": quantity, "subtotal": subtotal}
        )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    return {
        "basket_items": basket_items,
        "total": total,
        "delivery": delivery,
        "grand_total": grand_total,
        "plant_count": plant_count,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
    }
