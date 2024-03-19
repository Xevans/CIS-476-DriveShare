from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, CustomLoginView
from landing.views import Welcome
from .forms import LoginForm



urlpatterns = [
    path('/register/', RegisterView.as_view(), name='user-registration'),
    path('/login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=LoginForm), name='login'),
    path('/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]