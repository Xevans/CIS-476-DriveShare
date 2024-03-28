from django.urls import path, include
from .views import wallet

urlpatterns = [
    path('wallet/', wallet, name='users-wallet'),
]