from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [

    #/rulz/
    url(r'^', views.rules_home, name='rulz_home'),

    #rulz/index
    url(r'index/', views.Rulz_IndexView.as_view(), name='rulz_index'),

    #rulz/458
    url(r'^(?P<rulz_id>[0-9]+)$',views.Rulz_DetailView.as_view(),name='rulz_detail'),


    #/rulz/create
    url(r'create/$', views.RulzCreate.as_view(), name='rulz_create'),
]
