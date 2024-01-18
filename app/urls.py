from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("addque/", views.addQue, name='addque'),
    path('quiz_selection/', views.quiz_selection, name='quiz_selection'),
    path('result', views.result, name='result'),
    path('quiz_history/', views.quiz_history, name='quiz_history'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),

]
