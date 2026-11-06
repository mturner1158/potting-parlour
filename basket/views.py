from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from plants.models import Plant


def view_basket(request):
    """Renders the basket page"""

    template = 'basket/basket.html'

    return render(request, template)


@require_POST
def add_to_basket(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id, is_active=True)

    try:
        quantity = int(request.POST.get('quantity', 0))
    except ValueError:
        quantity = 0

    redirect_url = request.POST.get('redirect_url', '')

    if quantity < 1:
        messages.error(request, 'Please choose a valid quantity.')
        return redirect(redirect_url)

    basket = request.session.get('basket', {})
    key = str(plant.pk)

    if key in basket:
        basket[key] += quantity
        messages.success(
            request, f'Updated {plant.name} quantity to {basket[key]}'
        )
    else:
        basket[key] = quantity
        messages.success(request, f'Added {plant.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


@require_POST
def adjust_basket(request, plant_id):
    """Set a plant's amount in the basket (anything below 1 removes it)"""
    plant = get_object_or_404(Plant, pk=plant_id)
    quantity = int(request.POST.get("quantity"))

    basket = request.session.get("basket", {})
    key = str(plant.pk)

    if quantity > 0:
        basket[key] = quantity
        messages.success(
            request, f"Updated {plant.name} in your basket"
            )
    else:
        basket.pop(key, None)
        messages.success(
            request, f"Removed {plant.name} from your basket"
            )

    request.session["basket"] = basket
    return redirect("view_basket")


@require_POST
def remove_from_basket(request, plant_id):
    """Remove a plant from the basket"""
    basket = request.session.get("basket", {})

    if basket.pop(str(plant_id), None) is not None:
        plant = Plant.objects.filter(pk=plant_id).first()
        name = plant.name if plant else "Item"
        messages.success(
            request, f"Removed {name} from your basket"
            )

    request.session["basket"] = basket
    return redirect("view_basket")
