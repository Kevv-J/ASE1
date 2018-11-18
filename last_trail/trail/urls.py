from django.urls import path,include
from . import views
urlpatterns=[
    path('voter/',views.voter,name='trail.voter'),
    path('candidate/',views.candidate,name='trail.candidate'),
    path('result/',views.result,name='trail.result'),
    path('candidate_details/<int:pk>', views.candidate_details, name='candidate_details'),


]