from django.db import models

# Create your models here.

class Account(models.Model):
    login = models.CharField(max_length=100, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name = 'Пароль')
    group = models.IntegerField(verbose_name = 'Группа') # -1 - клиент 0 - Поставщик 1 - игрок

    def __str__(self):

        return f"{self.login} {self.password} {group}"

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
        ordering = ['-group']
