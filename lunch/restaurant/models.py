from django.db import models
from helpers.models import TrackingModel
from menu.models import Menu

class Restaurant(TrackingModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    menus = models.ManyToManyField(Menu, related_name='restaurants', blank=True)

    def __str__(self):
        return f'{self.name}'

    
# Create your models here.
