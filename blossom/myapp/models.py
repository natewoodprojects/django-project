from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Plant(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    water_ammount = models.DecimalField(decimal_places=0, max_digits=10)

    description = models.CharField(max_length=500)
    