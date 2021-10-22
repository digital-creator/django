from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)

class SupplierMaterials(models.Model):
    supplier = models.ForeignKey(Supplier, models.PROTECT, null=True)
    name_materials = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.IntegerField()
