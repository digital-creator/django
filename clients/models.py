from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
