from django.db import models

# Create your models here.
class Menuitems(models.Model):
    name = models.CharField(max_length= 200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()
    