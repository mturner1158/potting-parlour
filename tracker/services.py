from .models import UserPlant


def add_order_to_tracker(order):
    """Add plant from an order to the users tracker"""
    # check if a plant is already on the tracker
    if order.plants_added_to_tracker or not order.user_profile:
        return

    # add each plant in the order
    owner = order.user_profile.user
    tracked = []
    for item in order.lineitems.select_related("plant"):
        for _ in range(item.quantity):
            tracked.append(UserPlant(owner=owner, plant=item.plant, bought_plant=order))
    UserPlant.objects.bulk_create(tracked)

    order.plants_added_to_tracker = True
    order.save(update_fields=["plants_added_to_tracker"])
