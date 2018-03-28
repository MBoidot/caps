from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [
    url(r'home', views.rules_home, name='rulz_home'),
    url(r'create', views.RulzCreate.as_view(), name='rulz_create')
]
