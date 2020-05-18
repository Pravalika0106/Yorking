from django.contrib import admin
from django.urls import path,include
from Yorking import views

urlpatterns = [
    path('',views.index),
    path('form/',views.modelform),
    path('team_selection/',views.selection,name='selection'),
    path('edit_selection/',views.edit_selection,name='edit'),
    path('playerperfomance/',views.playerperfomance,name='update'),
]
