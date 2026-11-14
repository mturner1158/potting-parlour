from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import UserPlant
from .forms import UserPlantForm


@login_required
def view_tracker(request):
    """Shows tracker for plants the user has bought"""

    user_plants = request.user.owned_plants.select_related("plant", "bought_plant")
    total_plants = user_plants.count()

    template = "tracker/tracker.html"

    context = {
    "user_plants": user_plants,
    "total_plants": total_plants,
    "needs_water_count": sum(1 for p in user_plants if p.needs_water),
    }

    return render(request, template, context)


@login_required
def tracker_details(request, plant_id):
    """Show details of a users bought plant and uppdate tehm"""
    user_plant = get_object_or_404(
        UserPlant.objects.select_related("plant", "bought_plant"),
        pk=plant_id,
        owner=request.user,
    )

    if request.method == "POST":
        form = UserPlantForm(request.POST, instance=user_plant)
        if form.is_valid():
            form.save()
            messages.success(request, f'{user_plant.display_name} details have been updated')
            return redirect("tracker_details", plant_id=user_plant.id)
        messages.error(request, "Failed to update. Please review the form")
    else:
          form = UserPlantForm(instance=user_plant)


    template = "tracker/tracker_details.html"

    context = {
        "user_plant": user_plant,
        "form": form,
        "watering_history": user_plant.watering_logs.all()[:10],
    }

    return render(request, template, context)


@login_required
@require_POST
def water_plant(request, plant_id):
    user_plant = get_object_or_404(UserPlant, pk=plant_id, owner=request.user)
    user_plant.mark_watered()
    messages.success(request, f"{user_plant.display_name} watered!")

    return redirect("tracker_details", plant_id=user_plant.id)
