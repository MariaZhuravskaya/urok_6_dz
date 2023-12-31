from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verify, check_email, error, UserPassword

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/<int:id_user>', verify),
    path('check_email', check_email, name='check_email'),
    path('error', error, name='error'),


    path('password_reset', UserPassword.as_view(), name='password_reset'),

]