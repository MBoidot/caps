from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [
    url(r'home', views.rules_home, name='rulz_home'),
    #rulz/index
    url(r'index', views.IndexView.as_view(), name='rulz_index'),
    #rulz/number



    url(r'create/$', views.RulzCreate.as_view(), name='rulz_create'),
]
