from django.shortcuts import render

from .models import Plant, Category

# Create your views here.

def all_plants(request):
    plants = Plant.objects.all()


    template = "plants/plants.html"
    context = {
        "plants": plants
    }

    return render(request, template, context)