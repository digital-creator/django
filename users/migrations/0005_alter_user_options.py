# Generated by Django 3.2.8 on 2021-11-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
