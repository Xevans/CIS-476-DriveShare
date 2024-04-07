from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from pages.forms import SecurityQuestions
from users.models import Profile

# Create your views here.
def Welcome(request): 
    security_form = SecurityQuestions(request.POST)
    if request.user.is_authenticated:
        if request.user.profile.is_first_time == True: # do check in template

            if request.method == 'POST':
                security_form = SecurityQuestions(request.POST, instance=request.user.profile)
                
                if security_form.is_valid():
                    this_sq1 = security_form.cleaned_data['sq1']
                    this_sq2 = security_form.cleaned_data['sq2']
                    this_sq3 = security_form.cleaned_data['sq3']

                    # get the logged in user's profile
                    request.user.profile.sq1 = this_sq1
                    request.user.profile.sq2 = this_sq2
                    request.user.profile.sq3 = this_sq3
                    request.user.profile.is_first_time = False

                    request.user.profile.save()

                    redirect(to='welcome')

            else:
                security_form = SecurityQuestions(request.POST, instance=request.user.profile)




    return render(request, "welcome.html", {'security_form': security_form})
