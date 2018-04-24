from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'rulz'

urlpatterns = [

    #/rulz/
    url(r'^', views.rules_index.as_view(), name='rulz_index'),
    url(r'^index/$', views.rules_index.as_view(), name='rulz_index'),
    # /rulz/details
    url(r'^(?P<pk>[0-9]+)/$',views.rules_detail.as_view(),name='rulz_detail'),

    #rulz/create
    url(r'^create/',views.rules_create.as_view(),name='rulz_create')
]
