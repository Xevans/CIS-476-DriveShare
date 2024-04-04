from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UpdateBalanceForm
from .forms import ListingForm, RentalApplicationForm
from .models import Listings, RentalApplication, RentalTansactionHistory
from django.contrib import messages
from django.db.models import Q

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
            cost_per_day = listing_form.cleaned_data['cost_per_day']

            # need to attatch ownership to vehichle
            # assemble the new object
            new_listing = Listings.objects.create(owner_username=request.user.username, make=this_make, model=this_model, year=this_year, color=this_color, size_type=this_size_type, mileage=this_mileage, cost_per_day=cost_per_day)
            # save object
            print("here")
            new_listing.save()
            # set vehicle idea
            new_listing.vehicle_listing_id = new_listing.pk
            new_listing.save()

            return redirect(to='users-listings')
        
        else:
            print("not valid")
        
    else:
        listing_form = ListingForm(request.POST, instance=request.user.profile)

        this_user = request.user.username # get current user's username
        listings_from_this_user = Listings.objects.filter(Q(owner_username=this_user))

    return render(request, 'my_listings.html', {'listing_form': listing_form, 'current_user_listings': listings_from_this_user})

@login_required
def publicListings(request):
    if request.method == "POST":
        # sending an application
        rental_application_form = RentalApplicationForm(request.POST, instance=request.user.profile)

        
        if rental_application_form.is_valid():
            this_req_lease_length_days = rental_application_form.cleaned_data['req_lease_length_days']
            this_vehicle_id = request.POST['vehichle-id']
            this_borrower_username = request.user.username
            # search for listing by vehicle id
            print('here1')
            listing_object = Listings.objects.filter(Q(vehicle_listing_id=this_vehicle_id))
            # if found, exract info 
            if listing_object:
                print('here2')
                this_owner_username = listing_object[0].owner_username
                this_cost_per_day = listing_object[0].cost_per_day

                #construct application
                new_application = RentalApplication.objects.create(owner_username=this_owner_username, borrower_username=this_borrower_username, cost_per_day=this_cost_per_day, vehicle_listing_id=this_vehicle_id, req_lease_length_days=this_req_lease_length_days)
                new_application.save()
                print('success')
                return redirect(to='all-users-listings')

            else:
                print("failed to retrieve listing object")
                return redirect(to='all-users-listings')

            #construct application object


            #new_application = RentalApplication.objects.create()
            return redirect(to='all-users-listings')
    else:
        listings_from_all_users = Listings.objects.all()
        rental_application_form = RentalApplicationForm(request.POST, instance=request.user.profile)

        

    return render(request, 'listings.html', {'all_listings': listings_from_all_users, 'rental_application_form': rental_application_form})

