from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

TYPE_CHOICES = (
    ("Student", "Student"),
    ("Guest", "Guest"),
    ("Attendant", "Attendant"),
)

class Customer(models.Model):
    # user    = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=150, unique=True)
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
    password      = models.CharField(max_length=32) 
    address       = models.TextField(null=True, blank=True)
    type          = models.CharField(max_length=120, choices=TYPE_CHOICES, default="Guest")
    mobile        = models.CharField(max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return f'{self.first_name} Customer' 

    # def save(self):
    #     super().save()

    def get_address(self):
        if len(self.address) > 15:
            return self.address[:15] + " ...."
        return self.address
