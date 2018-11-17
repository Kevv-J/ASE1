from django.urls import path
from . import views

app_name="organiser_app"

urlpatterns=[

        path('index/', views.index, name="index"),
        path('candidate/', views.candidate_page, name='candidate'),
        path('voter/', views.voter_page, name='voter'),

]
