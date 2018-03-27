from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'shop'

urlpatterns = [
    url(r'^', views.shop_index, name='shop_index'),
]
