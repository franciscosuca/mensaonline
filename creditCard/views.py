"""
3. Modify the view

Import the the modules from rest_framework to call viewsets
Import the the modules from rest_framework.permissions to call modules for auth
Import the class from serializer file

"""

from creditCard.models import CreditCard
from creditCard.serializers import CreditCardSerializer
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from django.contrib.auth.mixins import LoginRequiredMixin

# Allowing any user to access the view
@permission_classes((AllowAny, ))

# View for user interface
class CreditCardViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer #Serelize data


