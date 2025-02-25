from django.db import models

# Create your models here.

class Boiler(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10, default='male')
    content = models.TextField(max_length=500)
