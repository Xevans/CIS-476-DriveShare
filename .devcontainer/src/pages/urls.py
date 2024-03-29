from django.urls import path, include
from .views import wallet, myListings

urlpatterns = [
    path('wallet/', wallet, name='users-wallet'),
    path('my_listings/', myListings, name='users-listings')
]