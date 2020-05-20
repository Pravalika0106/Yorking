from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Index'),
    path('TopPerfomance/',views.TopPerfomance),
    path('form/',views.form),
]
