from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=128)
    time = models.IntegerField()

    def __str__(self):
        return self.name


class ProductKit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество")
    time = models.IntegerField(verbose_name="Время")

    def __str__(self):
        return f"Комплект для {self.product} X {self.count}"

    @property
    def name(self):
        return self.__str__()

    @staticmethod
    def create(product: Product, count: int, time: int):
        return ProductKit.objects.create(product=product,
                                         count=count,
                                         time=time)
