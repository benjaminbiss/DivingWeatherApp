from django.db import models

# Create your models here.
class Replies(models.Model):
    review_pk = models.IntegerField(null=True, blank=True)
    diver_pk = models.IntegerField(null=True, blank=True)
    reply = models.CharField(max_length=250)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)