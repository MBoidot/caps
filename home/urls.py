from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'home'

urlpatterns = [
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^', views.HomeView, name='home'),
]
