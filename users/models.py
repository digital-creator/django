from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_client = models.BooleanField(null=True, verbose_name="Клиент")
    is_player = models.BooleanField(null=True, verbose_name="Игрок")
    is_supplier = models.BooleanField(null=True, verbose_name="Поставщик")

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
