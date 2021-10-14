from django.db import models

# Create your models here.


class HistoryActions(models.Model):
    name_action = models.CharField(max_length=150)
    summ_actions = models.CharField(max_length=100)
    balance = models.IntegerField()


class Materials(models.Model):
    name_materials = models.CharField(max_length=100)
    count_materials = models.IntegerField()

    def __repr__(self):
        return f"{self.id_player} {self.name_materials} {self.count_materials}"
