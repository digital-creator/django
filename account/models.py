from django.db import models

# Create your models here.

class Account(models.Model):
    is_unlimited = models.BooleanField()
    balance = models.IntegerField()

class Transaction(models.Model):
    from_account = models.IntegerField()
    to_account = models.IntegerField()
    offer = models.ForeignKey()
    time_stamp = models.DateTimeField()
