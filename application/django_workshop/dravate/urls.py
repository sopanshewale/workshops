from django.conf.urls import url
from dravate import views

urlpatterns = [url(r'^$', views.index, name='index'),]

