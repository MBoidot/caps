from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [

    #/rulz/
    url(r'^', views.rules_home, name='rulz_home'),

]
