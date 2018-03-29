from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [
    url(r'^', views.rules_home, name='rulz_home'),
    #rulz/index
    url(r'index', views.Rulz_IndexView.as_view(), name='rulz_index'),
    #rulz/ i.e. rulz/number
    url(r'^(?P<rulz_id>[0-9]+)$',views.Rulz_DetailView.as_view(),name='rulz_detail')

    url(r'create/$', views.RulzCreate.as_view(), name='rulz_create'),
]
