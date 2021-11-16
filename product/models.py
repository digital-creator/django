from django.db import models

# Create your models here.

class ProductKit(models.Model):
    name = models.CharField(verbose_name="Название комплекта", max_length=128)
    product_name = models.CharField(verbose_name="Название продукта", max_length=128)
    count = models.IntegerField(verbose_name="Количество")
    time = models.IntegerField(verbose_name="Время")

class Product(models.Model):
    name_product = models.ForeignKey(ProductKit, on_delete=models.CASCADE, max_length=128)
    time = models.IntegerField()
