from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'league'

urlpatterns = [

    url(r'^index/$', views.league_index.as_view(), name='league_index'),

]
