from django.db import models

from orders.models import Order

STATUS_CHOICES = (
    ("Paid", "Paid"),
    ("Unpaid", "Unpaid"),
)

class Invoice(models.Model):
    order       = models.ForeignKey(Order, on_delete = models.CASCADE)
    amount      = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    status      = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Paid")
    transaction = models.CharField(max_length=150, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True, auto_now=False)
    update      = models.DateTimeField(auto_now_add=False, auto_now=True)

