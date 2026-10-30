from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_plants, name='all_plants'),
    path("<slug:slug>/", views.plant_detail, name="plant_detail"),
]
