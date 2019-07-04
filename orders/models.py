from django.db import models

from customers.models import Customer
from menus.models import Menu

STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Aproved", "Aproved"),
    ("Canceled", "Canceled"),
)

class Order(models.Model):
    customer  = models.ForeignKey(Customer, on_delete = models.CASCADE)
    menu      = models.ManyToManyField(Menu)
    status    = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Pending")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update    = models.DateTimeField(auto_now_add=False, auto_now=True)

    

