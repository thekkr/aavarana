from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.SignUpView.as_view(),name='register'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('edit_profile/',views.EditProfileView.as_view(),name='edit_profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]