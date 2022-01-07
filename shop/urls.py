from django.urls import re_path
from django.contrib import admin
from . import views


app_name = 'shop'

urlpatterns = [
    re_path(r'^', views.shop_index, name='shop_index'),
]
