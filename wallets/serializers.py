"""
2. Create the serializer

Import the serializers module from rest_framework

"""
from rest_framework import serializers
from wallets.models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields="__all__"
