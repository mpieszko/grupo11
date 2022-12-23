from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.

# class UserRegisterView(generic.CreateView):
#     form_Class = UserCreationForm
#     template_name = 'log/register.html'
#     success_url = reverse_lazy('login')
    
