
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from .views import *
urlpatterns = [
    path('',FrontPage, name='FrontPage'),

    path('calories',CaloriesView, name='calories'),
    path('exercises',ExercisesView, name='exercises'),
    path('map',mapView,name='map'),

    path('recommendations',RecommendedView,name='recomendtaions'),

    path('login',LoginFrontView, name='front-login'),
    path('logout',logoutFrontView, name='front-logout'),
    path('register',RegisterFrontView,name='front-reg'),
]