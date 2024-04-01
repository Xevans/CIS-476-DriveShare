from django.db import models

# Create your models here.
class Listings(models.Model):
    owner_username = models.CharField(max_length=100, default="")
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField(default = 2010)
    size_type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    mileage = models.IntegerField(default=100)
