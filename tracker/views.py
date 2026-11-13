from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UserPlant


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

