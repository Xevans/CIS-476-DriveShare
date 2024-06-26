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
    cost_per_day = models.FloatField(default=50.00)
    is_available = models.BooleanField(default=True)
    vehicle_listing_id = models.IntegerField(default=-1) # to be set to the id value after creation


class Reviews(models.Model):
    sender = models.CharField(max_length=100, default="")
    recipient = models.CharField(max_length=100, default="")
    review_text = models.TextField(default="")
    make = models.CharField(max_length=30, default="")
    model = models.CharField(max_length=30, default="")
    year = models.IntegerField(default = 2010)
    req_lease_length_days = models.IntegerField(default=2)
    application_id = models.IntegerField(default=-1)
    review_id = models.IntegerField(default=-1)
    is_published = models.BooleanField(default=False)


class RentalApplication(models.Model):
    owner_username = models.CharField(max_length=100, default="")
    borrower_username = models.CharField(max_length=100, default="")
    cost_per_day = models.FloatField(default=50.00)
    vehicle_listing_id = models.IntegerField(default=-1)
    is_approved = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    req_lease_length_days = models.IntegerField(default=2)
    message = models.TextField(default="")
    application_id = models.IntegerField(default=-1)
    profile_id = models.IntegerField(default=-1)


class RentalTansactionHistory(models.Model):
    owner_username = models.CharField(max_length=100, default="")
    borrower_username = models.CharField(max_length=100, default="")
    cost_per_day = models.FloatField(default=0.00)
    vehicle_listing_id = models.IntegerField(default=-1)
    lease_length_days = models.IntegerField(default=2)
    is_returned = models.BooleanField(default=False)
    application_id = models.IntegerField(default=-1)





