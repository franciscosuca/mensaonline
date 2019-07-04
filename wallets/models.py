from django.db import models

from customers.models import Customer

STATUS_CHOICES = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
)

class Wallet(models.Model):
    customer      = models.ForeignKey(Customer, on_delete = models.CASCADE)
    # wallet_number = models.CharField(max_length=50, unique=True, null=True)
    wallet_number = models.CharField(max_length=50, null=True)
    balance       = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    status        = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Active")
    timestamp     = models.DateTimeField(auto_now_add=True, auto_now=False)
    update        = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    