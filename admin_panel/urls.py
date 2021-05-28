from django.urls import path
from .views import *


urlpatterns = [
    path('', adminPanelView, name='panel'),

    path('login', loginView, name='login'),
    path('logout', logoutView, name='logout'),
    path('auth-register', RegisterView, name='auth-register'),

    path('food-add', FoodAddView,name='food-add'),
    path('food-edit/<int:food_id>', FoodEditView,name='food-edit'),

    path('ex-add',ExAddView,name='ex-add'),
    path('ex-edit/<int:ex_id>', ExEditView,name='ex-edit'),
    ]