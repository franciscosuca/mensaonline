"""
2. Create the serializer

Import the serializers module from rest_framework

"""
from rest_framework import serializers
from menus.models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields="__all__"
