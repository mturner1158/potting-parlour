from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Plant, Category
from .forms import PlantForm


SORT_OPTIONS = {
    "name_asc": ("Name A-Z", "name"),
    "price_asc": ("Price low-high", "price"),
    "price_desc": ("Price high-low", "-price"),
    "newest": ("Newest", "-created_at"),
}



def all_plants(request):
    """ A view for all plants, including sorting and a search query """
    plants = Plant.objects.all()
    query = request.GET.get("q", "").strip()
    selected_categories = [c for c in request.GET.getlist("category") if c]
    light = request.GET.get("light", "")
    difficulty = request.GET.get("difficulty", "")
    pet_safe = request.GET.get("pet_safe", "")
    sort = request.GET.get("sort", "name_asc")

    if query:
        plants = plants.filter(
            Q(name__icontains=query)
            | Q(scientific_name__icontains=query)
            | Q(description__icontains=query)
            | Q(category__name__icontains=query)
        )

    if selected_categories:
        plants = plants.filter(category__slug__in=selected_categories)
    if light in Plant.Light.values:
        plants = plants.filter(light=light)
    else:
        light = ""
    if difficulty in Plant.Difficulty.values:
        plants = plants.filter(difficulty=difficulty)
    else:
        difficulty = ""
    if pet_safe == "1":
        plants = plants.filter(pet_safe=True)

    if sort not in SORT_OPTIONS:
        sort = "name_asc"
    plants = plants.order_by(SORT_OPTIONS[sort][1], "name")

    template = "plants/plants.html"
    context = {
        "plants": plants,
        "categories": Category.objects.all(),
        "light_choices": Plant.Light.choices,
        "difficulty_choices": Plant.Difficulty.choices,
        "sort_options": [(key, label) for key, (label, _) in SORT_OPTIONS.items()],
        "query": query,
        "selected_categories": selected_categories,
        "light": light,
        "difficulty": difficulty,
        "pet_safe": pet_safe,
        "current_sort": sort,
        "has_filters": bool(
            query or selected_categories or light or difficulty or pet_safe
        ),
    }

    return render(request, template, context)

def plant_detail(request, slug):
    plant = get_object_or_404(Plant, slug=slug, is_active=True)


    template = "plants/plants_detail.html"
    context = {
        "plant": plant
    }

    return render(request, template, context)


@login_required
def add_plant(request):
    """Allows super users to add plants to site"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only the store owners can do that.")
        return redirect("all_plants")

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            messages.success(request, "Plant added!")
            return redirect("plant_detail", slug=plant.slug)
        messages.error(request, "Failed to add the plant. Please check the form is valid.")
    else:
        form = PlantForm()

    template = "plants/plant_form.html"
    context = {
        "form": form,
        }

    return render(request, template, context)


@login_required
def edit_plant(request, plant_id):
    """Edit an existing plant on the site if youre a superuser"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only the store owners can do that.")
        return redirect("all_plants")

    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Plant updated!")
            return redirect("plant_detail", slug=plant.slug)
        messages.error(request, "Failed to update the plant. Please check the form is valid.")
    else:
        form = PlantForm(instance=plant)

    template = "plants/plant_form.html"
    context = {
            "form": form,
            "plant": plant,
            }
    return render(request, template, context)


@login_required
@require_POST
def delete_plant(request, plant_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only the store owners can do that.")
        return redirect("all_plants")

    plant = get_object_or_404(Plant, pk=plant_id)
    try:
        plant.delete()
    except ProtectedError:
        messages.error(
            request,
            "This plant has been ordered, so it can't be deleted. "
            "Untick 'Show in the shop' instead to hide it.",
        )
        return redirect("edit_plant", plant_id=plant.pk)

    messages.success(request, "Plant deleted!")
    return redirect("all_plants")
