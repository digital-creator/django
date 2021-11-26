# Generated by Django 3.2.8 on 2021-11-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211125_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'client'), (1, 'player'), (2, 'manufacturer')], default=1),
        ),
    ]