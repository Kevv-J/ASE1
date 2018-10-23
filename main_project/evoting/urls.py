from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='evoting-loginpage'),
    path('register/', views.register_page, name='evoting-registerpage'),
    path('registered/', views.home, name='evoting-register')
]