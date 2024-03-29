# Generated by Django 4.1.1 on 2022-10-04 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0005_alter_selectcar_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectcar',
            name='brand',
            field=models.CharField(choices=[('BMW', 'BMW'), ('MR', 'Mercedes'), ('AU', 'Audi')], default='BMW', max_length=30),
        ),
        migrations.AlterField(
            model_name='selectcar',
            name='car_model',
            field=models.CharField(choices=[('X1', 'X1'), ('X3', 'X3'), ('X5', 'X5'), ('X7', 'X7'), ('3S', '3-series'), ('5S', '5-series'), ('7S', '7-series'), ('A3', 'A3'), ('A4', 'A4'), ('A6', 'A6'), ('A8', 'A8'), ('Q2', 'Q2'), ('Q5', 'Q5'), ('Q7', 'Q7'), ('EC', 'E-class')], default='X1', max_length=30),
        ),
    ]
