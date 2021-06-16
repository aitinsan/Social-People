from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='exercises/')
    calories = models.TextField(default='')
    time = models.TextField(default='')