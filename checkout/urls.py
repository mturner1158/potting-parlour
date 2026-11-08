from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path("<slug:slug>/", views.checkout_success, name="checkout_success"),
]
