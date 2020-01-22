from django.conf.urls import url
from django.urls import path
from direct import views

app_name = 'direct'
urlpatterns = [
    path('<int:number>', views.position_detail, name='position_detail'),
    url(r'^choose/first_choice/$', views.choose_first),
    url(r'^choose/second_choice/$', views.choose_second),
]