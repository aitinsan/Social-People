from django.db import models
from django.contrib.auth.models import User
from .exercises import *
from .food import *

class UserRequestedCalories(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="user_reco",
                              )
    calo = models.TextField(default='')

class UserFood(models.Model):
    owner = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="user_food",
                                 )
    food = models.ForeignKey(Food,
                             on_delete=models.CASCADE,
                             related_name='user_food',
                             )

class UserExercises(models.Model):
    owner = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="user_exercises",
                                 )
    ex = models.ForeignKey(Exercise,
                             on_delete=models.CASCADE,
                             related_name='user_ex',
                             )
