from re import M
from django.db import models

# Create your models here.
class Locations(models.Model):
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    name = models.CharField(max_length=150)