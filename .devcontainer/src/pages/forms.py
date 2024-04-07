from django import forms
from .models import Listings, Reviews, RentalApplication, RentalTansactionHistory

class ListingForm(forms.ModelForm):
    make = forms.CharField(required=True, max_length=50)
    model = forms.CharField(required=True, max_length=50)
    year = forms.IntegerField(required=True)
    size_type = forms.CharField(required=True, max_length=30)
    color = forms.CharField(required=True, max_length=50)
    mileage = forms.IntegerField(required=True)
    cost_per_day = forms.FloatField(required=True)

    class Meta:
        model = Listings
        fields = ['make', 'model', 'year', 'size_type', 'color', 'mileage', 'cost_per_day']

class UpdateListingForm(forms.ModelForm):
    is_available = forms.BooleanField(required=False)
    cost_per_day = forms.FloatField(required=False)
    color = forms.CharField(required=False, max_length=50)
    mileage = forms.IntegerField(required=False)

    class Meta:
        model = Listings
        fields = ['is_available', 'cost_per_day', 'color', 'mileage']



class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Reviews
        fields = ['review_text']


class RentalApplicationForm(forms.ModelForm):
    req_lease_length_days = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = RentalApplication
        fields = ['req_lease_length_days', 'message']

