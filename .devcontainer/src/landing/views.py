from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.
class Welcome(TemplateView): # check user type then redirect to proper home page?
    template_name = "welcome.html"
