from django.shortcuts import render
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserLoginView(LoginView):
    template_name = 'registration/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    




