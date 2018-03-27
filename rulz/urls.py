from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'rulz'

urlpatterns = [
    url(r'^', views.rules_index, name='rulz_index'),
    url(r'create', views.RulzCreate.as_view(), name='rulz_create')
]
