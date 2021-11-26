from django.db import models
from enum import Enum

# Create your models here.

class OfferState(Enum):
    DONE = "Done"
    DELETED = "Deleted"
    ACTIVE = "Active"

class Offer(models.Model):
    price = models.IntegerField()
    time_stamp = models.DateTimeField()
    state = models.IntegerField()

class SaleOffer(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product_kit = models.CharField(max_length=128)
    count = models.IntegerField()

class PurchaseOffer(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product = models.CharField(max_length=128)
    count = models.IntegerField()
