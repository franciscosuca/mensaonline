"""
2. Create the serializer

Import the serializers module from rest_framework

"""
from rest_framework import serializers
from invoices.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields="__all__"
