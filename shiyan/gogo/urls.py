from django.conf.urls import url,include
from django.contrib import admin
import gogo
from gogo import views


urlpatterns = [
    url(r'^$',views.loginPage),
    url(r'^show/', views.show),
    url(r'login', views.loginPage2),
    url(r'^login/', views.show, name="show"),
]
