from django.contrib import admin
from django.urls import path, include
from apps.basic import views

urlpatterns = [
    path('', views.home_page, name='homePage')
]