# Generated by Django 4.1 on 2022-08-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SelectCar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand",
                    models.CharField(
                        choices=[("BMW", "BMW"), ("MR", "Mercedes")],
                        default="BMW",
                        max_length=30,
                    ),
                ),
                (
                    "car_model",
                    models.CharField(
                        choices=[("X1", "X1"), ("X2", "X2"), ("X3", "X3")],
                        default="X1",
                        max_length=30,
                    ),
                ),
            ],
        ),
    ]
