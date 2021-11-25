from django.db import models
from account.models import Account

class Bank(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    summ = models.IntegerField(default=0)
