from django.db import models
from offer.models import Offer
# Create your models here.

class Account(models.Model):
    is_unlimited = models.BooleanField()

class Transaction(models.Model):
    from_account = models.IntegerField()
    to_account = models.IntegerField()
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    summ = models.IntegerField(default=0, blank=True)

    def get_balance(self, account: Account):
        balance = self.objects.filter(from_account=account)
