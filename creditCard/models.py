from django.db import models

class CreditCard(models.Model):
    # cc_charge       =   models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    cc_name         =   models.TextField(max_length=50)  
    cc_number       =   models.CharField(max_length=16, unique=True)
    cc_valid_date   =   models.CharField(max_length=5, null=True)
    cc_code         =   models.CharField(max_length=3, unique=True, null=True)
    
    def __str__(self):
         return self.cc_number