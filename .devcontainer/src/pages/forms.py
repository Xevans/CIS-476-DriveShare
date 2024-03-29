from django import forms
from .models import Listings

class ListingForm(forms.ModelForm):
    make = forms.CharField()
    model = forms.CharField()
    year = forms.IntegerField()
    size_type = forms.CharField()
    color = forms.CharField()
    mileage = forms.IntegerField()

    class Meta:
        model = Listings
        fields = ['make', 'model', 'year', 'size_type', 'color', 'mileage']
