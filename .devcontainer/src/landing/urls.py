from django.urls import path, include
from .views import Welcome
from users.views import profile

urlpatterns = [
    path('', Welcome, name='welcome'),
]