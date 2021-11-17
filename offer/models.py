from django.db import models

# Create your models here.
class Offer(models.Models):
    price = models.IntegerField()
    time_stamp = models.DatetimeField()
    state = models.IntegerField()

class SaleOffer(models.Model):
    product_kit = models.CharField(max_length=128)
    count = models.IntegerField()

class PurchaseOffer(models.Model):
    product = models.CharField(max_length=128)
    count = models.IntegerField()
    