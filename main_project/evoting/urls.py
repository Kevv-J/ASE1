from django.urls import path
from evoting import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('base/', user_views.base, name='base'),
    path('home/', user_views.home, name='evoting-home'),
    path('register/', user_views.register, name='evoting-register'),
    path('voter_login/', user_views.voter_login, name='evoting-voter-login'),
    path('organiser_login/', user_views.orgainser_login, name='evoting-organiser-login'),
    path('logout/', user_views.user_logout, name='evoting-logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name=''), name='evoting1-logout'),
    path('profile/', user_views.profile, name='evoting-user-profile'),
    path('activate/<uidb64>/<token>', user_views.activate, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='voters/password_reset.html'),
         name='pass-reset'
    ),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
       template_name='voters/password_reset_done.html'),
         name='password_reset_done'
    ),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(
        template_name='voters/password_reset_confirm.html'),
         name='password_reset_confirm'
    ),

]
