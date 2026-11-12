from django import forms
from django.utils.text import slugify

from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = (
            "category",
            "name",
            "scientific_name",
            "description",
            "price",
            "image",
            "image_url",
            "light",
            "difficulty",
            "watering_interval_days",
            "pet_safe",
            "is_active",
        )
        labels = {
            "image": "Upload an image",
            "image_url": "Or link to an image (optional)",
            "light": "Light needs",
            "difficulty": "Care difficulty",
            "watering_interval_days": "Days between watering",
            "pet_safe": "Pet safe",
            "is_active": "Show in the shop",
        }
        help_texts = {
            "is_active": "Untick to hide this plant without deleting it.",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_name(self):
        """Ensure slugs are unique"""
        name = self.cleaned_data["name"].strip()
        clash = Plant.objects.filter(slug=slugify(name)).exclude(pk=self.instance.pk)
        if clash.exists():
            raise forms.ValidationError("A plant with this name already exists.")
        return name

    def clean_price(self):
        """Ensure price is more than 0"""
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("The price must be more than £0.")
        return price
