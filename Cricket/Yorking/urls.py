from django.contrib import admin
from django.urls import path,include
from Yorking import views

urlpatterns = [
    path('',views.index),
    path('form/',views.modelform,name='index'),
    path('form_check/',views.form_check,name='form_check'),
    path('team_selection/',views.selection,name='selection'),
    path('check_constrains_1' , views.check_constrains_1,name='constrains'),
    path('perfomance_one_update/',views.perfomance_one_update),
    path('perfomance_one_save/',views.perfomance_one_save,name='perfomance_one_save'),

    path('edit_selection/',views.edit_selection,name='edit'),
    path('playerperfomance/',views.playerperfomance,name='update'),
    path('check_constrains/',views.check_constrains,name='check'),
    path('perfomance_update/',views.perfomance_update,name='perfomance'),
    path('perfomance_save/',views.perfomance_update_save,name='perfomance_save'),

    path('top_performers/',views.top_performers,name='top_performers'),


    #Integrating Swethas Code:
    path('team/',views.select_team,name="select_team"),
    path('players/',views.players_list,name="playerss"),
    path('validations/',views.user_team_validation,name='user_team_validation'),
    path('user_team/',views.user_team,name="user_team"),
    path('dashboard/',views.dashboard,name="dashboard"),


	path('test/',views.test),

    #Integrating Abhigna's code:
    path('user_point_calculation/',views.user_point_calculation),
    path('leaderboard_match/',views.leaderboard_match),
    path('leaderboard/',views.leaderboard,name='leaderboard_display'),



    path('User_Auth/',views.User_Auth),
    path('signup/',views.signup,name='signup')
]
