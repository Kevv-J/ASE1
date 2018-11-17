from django.urls import path
from organiser_app import views

app_name="organiser_app"

urlpatterns=[

        path('index/',views.index,name="index"),
        path('candidate/',views.candidate_page,name='candidate'),
        path('index1/',views.main_page,name='mainpage'),
        path('election/',views.election,name="election"),
        path('addelection/',views.addelection,name="addelection")

]
