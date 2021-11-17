from django.db import models

# Create your models here.

class Account(models.Model):
    is_unlimited = models.BooleanField()
    balance = models.IntegerField()

class Transaction(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    offer = None # К чему относится эта переменная?
    time_stamp = models.DateTimeField()
