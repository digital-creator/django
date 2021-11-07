# Generated by Django 3.2.8 on 2021-11-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211107_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(null=True, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_player',
            field=models.BooleanField(null=True, verbose_name='Игрок'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_supplier',
            field=models.BooleanField(null=True, verbose_name='Поставщик'),
        ),
    ]
