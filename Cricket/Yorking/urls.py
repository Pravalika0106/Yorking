from django.contrib import admin
from django.urls import path,include
from Yorking import views

urlpatterns = [
    path('',views.index),
    path('form/',views.modelform,name='index'),
    path('form_check/',views.form_check,name='form_check'),
    path('team_selection/',views.selection,name='selection'),
    path('check_constrains_1' , views.check_constrains_1,name='constrains'),
    path('edit_selection/',views.edit_selection,name='edit'),
    path('playerperfomance/',views.playerperfomance,name='update'),
    path('check_constrains/',views.check_constrains,name='check'),
    path('perfomance_update/',views.perfomance_update,name='perfomance'),
]
