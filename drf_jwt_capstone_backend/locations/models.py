from django.db import models

# Create your models here.
class Locations(models.Model):
    latitude = models.IntegerField(max_length=7)
    longitude = models.IntegerField(max_length=7)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)