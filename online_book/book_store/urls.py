
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path('search_category', views.search_category, name='search_category'),
    path('checkout', views.checkout, name='checkout'),
    path('status', views.status, name='status')

]