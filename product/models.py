from django.db import models

# Create your models here.

class ProductKit(models.Model):
    name = models.CharField(verbose_name="Название комплекта")
    product = models.CharField(verbose_name="Название продукта")
    count = models.IntegerField(verbose_name="Количество")
    time = models.IntegerField(verbose_name="Время")

class Product(models.Model):
    name = models.ForeignKey(ProductKit, on_delete=models.CASCADE)
    time = models.IntegerField()
