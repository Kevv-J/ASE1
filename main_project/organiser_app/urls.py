from django.urls import path
from . import views

app_name="organiser_app"

urlpatterns=[

        path('index/',views.index,name="index"),
        path('candidate/',views.candidate_page,name='candidate'),
        path('index1/',views.main_page,name='mainpage'),
        path('election/',views.election,name="election"),
        path('addelection/',views.addelection,name="addelection"),
        path('voter_region_page/add_voter/', views.add_voter, name='add_voter'),
        path('voter_region_page/', views.voter_region_page, name='voter_region_page'),
        path('voter_region_page/search_voter', views.search_voter, name='search_voter'),


]
