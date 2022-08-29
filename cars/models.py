from django.db import models
import datetime
from dealers.models import Dealer
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=100)
    CATEGORY = (
            ('New','New'),
            ('Used','Used')
        )
    category = models.CharField(max_length=50, choices=CATEGORY)
    image_main = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)

    miles = models.IntegerField(blank=True, null=True)
    TRANSMISSION = (
                ('Manual','Manual'),
                ('Automatic','Automatic')
    )

    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    YEAR_CHOICES = [(r,r) for r in range(2005, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    power = models.IntegerField()
    fuel = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs = {
                        'car_id':self.id
        })
