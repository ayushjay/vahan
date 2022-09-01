from django.db import models

#TODO add second dropdown based on first one
 
class SelectCar(models.Model):
    BRANDS = (
        ('BMW','BMW'),
        ('MR','Mercedes'),
        ('HN','Honda'),
    )
    brand = models.CharField(max_length=30,
                  choices=BRANDS,
                  default="BMW")
    CAR_MODELS = (
        ('X1','X1'),
        ('X2','X2'),
        ('X3','X3'),
        ('AM','Amaze'),

    )

    car_model = models.CharField(max_length=30,
                  choices=CAR_MODELS,
                  default="X1")



