from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Plant, Category


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
