from django.urls import path
from .views import RegisterView
from landing.views import Welcome

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-registration')
]