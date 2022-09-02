from django.db import models

#TODO add second dropdown based on first one
 
class SelectCar(models.Model):
    BRANDS = (
        ('BMW','BMW'),
        ('MR','Mercedes'),
        ('HN','Honda'),
        ('AU','Audi'),
        
    )
    brand = models.CharField(max_length=30,
                  choices=BRANDS,
                  default="BMW")
    CAR_MODELS = (
        ('X1','X1'),
        ('X3','X3'),
        ('X5','X5'),
        ('X7','X7'),
        ('3S','3-series'),
        ('5S','5-series'),
        ('7S','7-series'),
        ('A3','A3'),
        ('A4','A4'),
        ('A6','A6'),
        ('A8','A8'),
        ('Q2','Q2'),
        ('Q5','Q5'),
        ('Q7','Q7'),
        ('AM','Amaze'),
        ('EC','E-class'),


    )

    car_model = models.CharField(max_length=30,
                  choices=CAR_MODELS,
                  default="X1")



