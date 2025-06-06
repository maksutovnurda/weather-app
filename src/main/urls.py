from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('last_searches/', views.last_searches, name='last_searches'),
]
