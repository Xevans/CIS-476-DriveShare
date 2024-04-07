from django.urls import path, include
from .views import wallet, myListings, publicListings, dashboard, rentalHistory, myReviews

urlpatterns = [
    path('wallet/', wallet, name='users-wallet'),
    path('my_listings/', myListings, name='users-listings'),
    path('find_a_DriveShare/', publicListings, name='all-users-listings'),
    path('dashboard/', dashboard, name='dashboard'),
    path('rental_history/', rentalHistory, name='users-history'),
    path('reviews/', myReviews, name='users-reviews'),
]