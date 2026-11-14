from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_tracker, name='view_tracker'),
    path("<int:plant_id>/", views.tracker_details, name="tracker_details"),
    path("<int:plant_id>/water/", views.water_plant, name="water_plant"),
    path("<int:plant_id>/remove/", views.remove_plant, name="remove_plant"),
]
