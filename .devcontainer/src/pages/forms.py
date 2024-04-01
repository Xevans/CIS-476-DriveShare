from django import forms
from .models import Listings

class ListingForm(forms.ModelForm):
    owner_username = forms.CharField()
    make = forms.CharField()
    model = forms.CharField()
    year = forms.IntegerField()
    size_type = forms.CharField()
    color = forms.CharField()
    mileage = forms.IntegerField()

    class Meta:
        model = Listings
        fields = ['owner_username', 'make', 'model', 'year', 'size_type', 'color', 'mileage']
