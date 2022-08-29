from django.db import models

# Create your models here.
class Dealer(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images')
    description = models.TextField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
