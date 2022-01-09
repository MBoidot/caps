from django.urls import re_path
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [

    #/rulz/
    re_path(r'^', views.rules_home, name='rulz_home'),

    #rulz/index
    re_path(r'index/', views.Rulz_IndexView.as_view(), name='rulz_index'),

    #rulz/458
    re_path(r'^(?P<rulz_id>[0-9]+)$',views.Rulz_DetailView.as_view(),name='rulz_detail'),


    #/rulz/create
    re_path(r'create/$', views.RulzCreate.as_view(), name='rulz_create'),
]
