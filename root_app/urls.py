from django.urls import re_path, include
from django.contrib import admin
from home import views
from rulz import views
from shop import views
from . import views
from home import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rules/',include('rulz.urls')),
    re_path(r'^shop/',include('shop.urls')),
    re_path(r'^',include('home.urls')),
]
