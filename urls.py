from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # --- Authentication Pages ---
    path('signup/', views.signup, name='signup'),
    path('registration_successful/', views.registration_successful, name='registration_successful'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # --- Password Reset Flow (Complete 4 Steps) ---
    
    # 1. Reset Form (Jo aapke paas pehle se tha)
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'
    ), name='password_reset'),

    # 2. Email Sent Success Message (Yeh MISSING tha - Error ki wajah)
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    # 3. Link Click Page (Jahan naya password dalenge)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),

    # 4. Password Change Success
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]