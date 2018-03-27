from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',include('home.urls')),
    url(r'^$',views.HomeView),
]
