from django import forms
from .models import Listings

class ListingForm(forms.ModelForm):
    make = forms.CharField(required=True, max_length=50)
    model = forms.CharField(required=True, max_length=50)
    year = forms.IntegerField(required=True)
    size_type = forms.CharField(required=True, max_length=30)
    color = forms.CharField(required=True, max_length=50)
    mileage = forms.IntegerField(required=True)

    class Meta:
        model = Listings
        fields = ['make', 'model', 'year', 'size_type', 'color', 'mileage']
