# menu/models.py
from django.db import models
from helpers.models import TrackingModel


class MenuItem(TrackingModel):
    """
    Item in menu, have ManyToMany relation, because one item can be in several restaurants, like Caesar salad which is in every restaurant exists
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
   
    def __str__(self):
        return self.name

class Menu(TrackingModel):
    """
    A menu model, that have relations OneToMany for Restaurant and ManyToMany for items in menu
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, related_name='menus')
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.restaurant}"



# ... Other models and code related to the menu app ...
