# Generated by Django 4.1.1 on 2022-11-04 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
    ]