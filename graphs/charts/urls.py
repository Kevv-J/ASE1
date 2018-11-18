from django.urls import path,include,re_path
from charts import views
from django.conf.urls import url
urlpatterns=[
    url(r'^index1/',views.index1,name='index1'),
    url(r'^get_feedback/',views.get_feedback,name='get_feedback'),

]
