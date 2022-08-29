from django.db import models
from dealers.models import Dealer
import datetime



# Create your models here.
class Listing(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    kilometri = models.IntegerField()
    potrosnja = models.IntegerField()
    vrsta = models.CharField(max_length=100)
    YEAR_CHOICES = [(r,r) for r in range(2005, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    snaga = models.IntegerField()
    price = models.IntegerField()
    CATEGORY = (
            ('New', 'New'),
            ('Used', 'Used')
        )
    category = models.CharField(max_length= 50, null=True, choices=CATEGORY)
    image_main = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
