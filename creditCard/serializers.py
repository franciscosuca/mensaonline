"""
2. Create the serializer

Import the serializers module from rest_framework

"""
from rest_framework import serializers
from creditCard.models import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=CreditCard
        fields="__all__"
