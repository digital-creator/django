from enum import Enum

from django.db import models

from product.models import ProductKit
from users.models import User


class OfferState(Enum):
    DONE = "Done"
    DELETED = "Deleted"
    ACTIVE = "Active"


class Offer(models.Model):
    price = models.IntegerField()
    timestamp = models.DateTimeField()
    state = models.CharField(max_length=16, choices=[
        (tag, tag.value) for tag in OfferState
    ], default=OfferState.ACTIVE)


class SaleOffer(models.Model):
    seller = models.ForeignKey(User, models.CASCADE)
    product_kit = models.ForeignKey(ProductKit, models.CASCADE)
    # count = models.IntegerField()
    offer = models.OneToOneField(Offer, models.CASCADE)


class PurchaseOffer(models.Model):
    customer = models.ForeignKey(User, models.CASCADE)
    product = models.CharField(max_length=128)
    # count = models.IntegerField()
    offer = models.OneToOneField(Offer, models.CASCADE)
