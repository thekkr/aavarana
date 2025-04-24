from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignUpForm , EditProfileForm , ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.views import View
# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Add the current user to the context
        return context

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
class EditProfileView(LoginRequiredMixin, View):
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request):
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })

    def post(self, request):
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect(self.success_url)

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('profile')  # Redirect to the profile page after password change
    
class UserLoginView(LoginView):
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    




