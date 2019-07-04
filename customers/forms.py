from django import forms
from django.contrib.auth.models import User
from . models import Customer

"""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
"""


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email_address', 'address', 'type', 'mobile']