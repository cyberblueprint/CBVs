from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^hello/$', views.HelloWorldView.as_view(), name='hello'),
    url(r'teams/', include('teams.urls', namespace='teams')),
]
