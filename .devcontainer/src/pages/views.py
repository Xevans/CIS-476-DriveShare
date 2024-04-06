from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UpdateBalanceForm
from .forms import ListingForm, RentalApplicationForm
from .models import Listings, RentalApplication, RentalTansactionHistory
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.messages.views import SuccessMessageMixin


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def dashboard(request):
    this_user_username = request.user.username

    if request.method == 'POST':
        
        print("here1")
        this_application_id = request.POST['application-id']

        # retrieve application and borrower user objects
        print(this_application_id)
        application = RentalApplication.objects.filter(application_id=this_application_id)
        
        this_application = application[0]

        rental_total_cost = this_application.cost_per_day * this_application.req_lease_length_days
        this_borrower = Profile.objects.filter(id=this_application.profile_id)
        this_borrower = this_borrower[0]


        # check sufficient funds of borrower [ <- dont check, this needs to happen on the borrower's side either furing applying or on acceptance of approval]
        this_borrower.balance = this_borrower.balance - rental_total_cost
        this_borrower.save()

        # pay owner of vehicle
        request.user.profile.balance += rental_total_cost
        request.user.profile.save()

        # set is_available for the listing to false.
        listing = Listings.objects.filter(vehicle_listing_id=this_application.vehicle_listing_id)
        this_listing = listing[0]
        this_listing.is_available = False
        this_listing.save()

        
        this_application.is_approved = True
        this_application.save()
        
        new_rental_history = RentalTansactionHistory.objects.create(owner_username=this_user_username, borrower_username=this_application.borrower_username, cost_per_day=this_application.cost_per_day, vehicle_listing_id=this_application.vehicle_listing_id, lease_length_days=this_application.req_lease_length_days, application_id=this_application_id)
        new_rental_history.save()
        
        messages.success(request, f'You Approve your Driveshare! ${rental_total_cost} has been deposited into your account')


        # deduct and pay members (return error message if failure and redirect)
        # update to approve status if valid and redirect.

        return redirect(to='dashboard')

    else:
        user_listings = Listings.objects.filter(Q(owner_username=this_user_username)) # filter by usename
        user_applications_outgoing = RentalApplication.objects.filter(Q(borrower_username=this_user_username)) # filter by borrower == this user
        user_applications_incoming = RentalApplication.objects.filter(Q(owner_username=this_user_username)) # filter by owner == this user
        # reviews TBD
        #DMs TBD


    return render(request, 'dashboard.html', {'user_listings': user_listings, 'user_applications_outgoing': user_applications_outgoing, 'user_applications_incoming': user_applications_incoming})


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
            new_listing.save()
            # set vehicle id
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
            this_message = rental_application_form.cleaned_data['message']
            this_vehicle_id = request.POST['vehichle-id']
            this_borrower_username = request.user.username
            # search for listing by vehicle id
            listing_object = Listings.objects.filter(Q(vehicle_listing_id=this_vehicle_id))
            # if found, exract info 
            if listing_object:
                this_owner_username = listing_object[0].owner_username
                this_cost_per_day = listing_object[0].cost_per_day

                #construct application
                new_application = RentalApplication.objects.create(owner_username=this_owner_username, borrower_username=this_borrower_username, cost_per_day=this_cost_per_day, vehicle_listing_id=this_vehicle_id, req_lease_length_days=this_req_lease_length_days, message=this_message)
                new_application.save()
                # set application id
                new_application.application_id = new_application.pk
                new_application.profile_id = request.user.profile.pk
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

