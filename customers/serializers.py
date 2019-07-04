"""
2. Create the serializer

Import the serializers module from rest_framework

"""
from rest_framework import serializers
from django.contrib.auth.models import User
from customers.models import Customer

from django.contrib.auth.hashers import make_password

class CustomerSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
        #help_text='Leave empty if no change needed',
        #style={'input_type': 'password', 'placeholder': 'Password'}
    )
    

    class Meta:
        model=Customer
        #fields="__all__"
        fields=('first_name', 'last_name', 'email_address', 'password', 'address', 'type', 'mobile')

    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(CustomerSerializer, self).create(validated_data)    

       
