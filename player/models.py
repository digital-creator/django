from django.db import models

# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название команды')
    balance = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ('name',)


class HistoryActions(models.Model):
    player = models.ForeignKey(Players, on_delete=models.PROTECT, null=True)
    name_action = models.CharField(max_length=150)
    summ_actions = models.CharField(max_length=100)
    balance = models.IntegerField()


class PlayersMaterials(models.Model):
    player = models.ForeignKey(Players, on_delete=models.PROTECT)
    name_materials = models.CharField(max_length=100)
    count_materials = models.IntegerField()
