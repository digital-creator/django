# Generated by Django 3.2.8 on 2021-10-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20211022_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
