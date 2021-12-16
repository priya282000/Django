
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_render, name='login_render'),
    path('login', views.login, name='login'),
    path('reg_render', views.reg_render, name='reg_render'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home')

]