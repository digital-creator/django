from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CLIENT = 0
    PLAYER = 1
    MANUFACTURER = 2
    ROLES = [
        (CLIENT, 'client'),
        (PLAYER, 'player'),
        (MANUFACTURER, 'manufacturer')

    ]
    role = models.IntegerField(choices=ROLES, default=1)
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
