from django.contrib import admin
from django.urls import path
from lohsite import views

urlpatterns = [
    path('', views.index),
    path('donate',views.donate),
    path('success',views.success,name='success')
]