from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'rulz'

urlpatterns = [

    #/rulz/
    url(r'^$', views.rules_index.as_view(), name='rulz_index'),
    url(r'^index/$', views.rules_index.as_view(), name='rulz_index'),
    # /rulz/details
    url(r'^(?P<pk>\d+)/$',views.rules_detail.as_view(),name='rulz_detail'),

    #rulz/create
    url(r'^create/',login_required(views.rules_create.as_view()),name='rulz_create'),
]
