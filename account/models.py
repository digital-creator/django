from django.db import models

from offer.models import Offer


class Account(models.Model):
    is_unlimited = models.BooleanField(default=False)

    @property
    def balance(self):
        return 99999999999


class Transaction(models.Model):
    from_account = models.ForeignKey(Account, models.CASCADE, related_name="from_account")
    to_account = models.ForeignKey(Account, models.CASCADE, related_name="to_account")
    offer = models.ForeignKey(Offer, models.CASCADE)
    timestamp = models.DateTimeField()
