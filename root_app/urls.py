from django.conf.urls import url, include
from django.contrib import admin
from home import views
from rulz import views
from shop import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',include('home.urls')),
    url(r'^rules/',include('rulz.urls')),
    url(r'^shop/',include('shop.urls')),

    url(r'^$',views.HomeView),
]
