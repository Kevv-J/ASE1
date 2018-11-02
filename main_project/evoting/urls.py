from django.urls import path, re_path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', user_views.home, name='evoting-home'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='evoting-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/logout.html'), name='evoting-logout'),
    path('register/', user_views.register, name='evoting-register'),
    path('profile/', user_views.profile, name='evoting-user-profile')
]
