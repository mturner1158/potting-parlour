from django import forms
from .models import Profile


# started with boutique ado form and modified for my model
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
        }

        self.fields['default_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0  \
                    profile-form-input'
            )
            self.fields[field].label = False
