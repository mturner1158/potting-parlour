from django import forms
from .models import UserPlant


class UserPlantForm(forms.ModelForm):
    """Allows users to input details on their plants"""

    class Meta:
        model = UserPlant
        fields = ("nickname", "notes")
        labels = {
            "nickname": "Nickname",
            "notes": "Notes",
        }
