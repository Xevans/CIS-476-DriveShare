from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UpdateBalanceForm
from .forms import ListingForm
from .models import Listings
from django.contrib import messages

# Create your views here.

@login_required
def wallet(request):
    return render(request, 'wallet.html')


@login_required
def wallet(request):
    if request.method == 'POST':
        balance_form = UpdateBalanceForm(request.POST, instance=request.user.profile)

        if balance_form.is_valid():
            #balance_form.save()
            messages.success(request, 'Your balance has been updated successfully')
            # do addition for user balance with the return value in request
            request.user.profile.balance += balance_form.cleaned_data['balance']
            request.user.save()
            return redirect(to='users-wallet')
        
    else:
        balance_form = UpdateBalanceForm(instance=request.user.profile)

    return render(request, 'wallet.html', {'balance_form': balance_form})

@login_required
def myListings(request):
    return render(request, 'my_listings.html')

@login_required
def myListings(request):
    if request.method == 'POST':
        listing_form = ListingForm(request.POST, instance=request.user.profile)

        if listing_form.is_valid():
            messages.success(request, 'Your listing was added successfully.')

            this_make = listing_form.cleaned_data['make']
            this_model = listing_form.cleaned_data['model']
            this_year = listing_form.cleaned_data['year']
            this_color = listing_form.cleaned_data['color']
            this_mileage = listing_form.cleaned_data['mileage']
            this_size_type = listing_form.cleaned_data['size_type']

            # assemble the new object
            
            # save object

            return redirect(to='users-listings')
        
    else:
        listing_form = ListingForm(request.POST, instance=request.user.profile)

    return render(request, 'my_listings.html', {'listing_form': listing_form})
