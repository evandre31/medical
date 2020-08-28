from django.urls import path, include

from accounts import views
from accounts.views import login_view, logout_view
from django.conf.urls import url  # changement de mot de passe
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth import views as auth_views  # paquet de views user _________

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('login/',
    #      auth_views.LoginView.as_view(template_name='accounts/registration/login.html'),
    #      name='login'),
    # path('logout/',
    #      auth_views.LogoutView.as_view(template_name='accounts/registration/logged_out.html'),
    #      name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    # path('change_password/', views.change_password, name='change_password'),_________________
    path('change_password/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/registration/change_password.html',
             success_url='/accounts/change_password_done/'),
         name='change_password'),
    path('change_password_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/registration/change_password_done.html'),
         name='change_password_done'),
    # password-rest_______________________________________________________________________
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/registration/password_reset_form.html',
        subject_template_name='accounts/registration/password_reset_subject.txt',
        email_template_name='accounts/registration/password_reset_email.html',
        success_url='done', ), name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/registration/password_reset_done.html'),
         name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/registration/password_reset_confirm.html',
        success_url='/accounts/password_reset_complete'),
         name="password_reset_confirm"),
    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/registration/password_reset_complete.html'),
         name="password_reset_complete"),
]
