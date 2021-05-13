from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='food/images/')
    calories = models.TextField()
    proteins = models.TextField()
    fats = models.TextField()
    carbo = models.TextField()
