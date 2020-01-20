from django.conf.urls import url
from direct import views

app_name = 'direct'
urlpatterns = [
    url(r'^choose/first/$', views.choose_first),
    url(r'^choose/second/$', views.choose_second),
]