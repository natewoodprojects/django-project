from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    water_ammount = models.DecimalField(decimal_places=0, max_digits=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Users(models.Model):
    email = models.CharField(max_length=200)



class Plants(models.Model):
    user_id = models.DecimalField(decimal_places=0, max_digits=10)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    light = models.CharField(max_length=200)
    water = models.CharField(max_length=200)
    humidity = models.CharField(max_length=200)
    soil = models.CharField(max_length=200)
    fertilizer = models.CharField(max_length=200)    
    toxcicity = models.BooleanField()
    notes = models.CharField(max_length=10000)
