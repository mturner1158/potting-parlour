from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.all_plants, name='all_plants'),
    path("add/", views.add_plant, name="add_plant"),
    path("edit/<int:plant_id>/", views.edit_plant, name="edit_plant"),
    path("delete/<int:plant_id>/", views.delete_plant, name="delete_plant"),
    path("<slug:slug>/", views.plant_detail, name="plant_detail"),
]
