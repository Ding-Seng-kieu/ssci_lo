from django.conf.urls import url
from direct import views

app_name = 'direct'
urlpatterns = [
    url(r'^choose/first_choice/$', views.choose_first),
    url(r'^choose/second_choice/$', views.choose_second),
]