from django.conf.urls import url
from django.contrib import admin

from . import views
from django.contrib.auth.views import login, logout


app_name = 'home'

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'home/login.html'},name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^', views.HomeView, name='home'),
]
