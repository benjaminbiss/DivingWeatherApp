from django.db import models

# Create your models here.
class Locations(models.Model):
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)