from django.shortcuts import render, get_object_or_404

from .models import Plant, Category

# Create your views here.

def all_plants(request):
    plants = Plant.objects.all()


    template = "plants/plants.html"
    context = {
        "plants": plants
    }

    return render(request, template, context)

def plant_detail(request, slug):
    plant = get_object_or_404(Plant, slug=slug, is_active=True)


    template = "plants/plants_detail.html"
    context = {
        "plant": plant
    }

    return render(request, template, context)