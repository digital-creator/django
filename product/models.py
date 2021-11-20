from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    time = models.IntegerField()

    def __str__(self):
        return self.name


class ProductKit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество")
    time = models.IntegerField(verbose_name="Время")

    def __str__(self):
        return f"Комплект для {self.product.name} x {self.count}"

    @property
    def name(self):
        return self.__str__()
