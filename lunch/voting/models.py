from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Menu
from employee.models import Employee

class MenuVote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['menu', 'employee']

    def __str__(self):
        return f'{self.employee.username} voted for {self.menu.name}'
    
    def num_votes(self):
        return self.menus.count()

# Create your models here.
