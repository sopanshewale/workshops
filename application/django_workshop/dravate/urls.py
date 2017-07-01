from django.conf.urls import url
from dravate import views

urlpattern = [url(r'^$', views.index, name='index'),]

