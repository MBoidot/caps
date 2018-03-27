from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'rulz'

urlpatterns = [
    url(r'^', views.rules_index, name='rulz_index'),
]
