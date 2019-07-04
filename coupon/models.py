from django.db import models

class Coupon(models.Model):
    number  =   models.CharField(max_length=50, unique=True)

    def __str__(self):
         return self.number