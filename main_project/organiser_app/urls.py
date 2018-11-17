from django.urls import path
from . import views

app_name="organiser_app"

urlpatterns=[

        path('index/',views.index,name="index"),
        path('candidate/',views.candidate_page,name='candidate'),
        path('index1/',views.main_page,name='mainpage'),
        path('election/',views.election,name="election"),
<<<<<<< HEAD
        path('addelection/',views.addelection,name="addelection")
=======
        path('voter/', views.voter_page, name='voter'),
>>>>>>> 98bbeb73bbeba6dc911f91b0fb4723606462537d

]
