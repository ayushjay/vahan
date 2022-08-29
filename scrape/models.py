from django.db import models

#TODO add second dropdown based on first one
 
class SelectCar(models.Model):
    BRANDS = (
        ('BMW','BMW'),
        ('MR','Mercedes')
    )
    brand = models.CharField(max_length=30,
                  choices=BRANDS,
                  default="BMW")
    CAR_MODELS = (
        ('X1','X1'),
        ('X2','X2'),
        ('X3','X3')

    )

    car_model = models.CharField(max_length=30,
                  choices=CAR_MODELS,
                  default="X1")



