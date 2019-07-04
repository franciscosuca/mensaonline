from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView

from . models import Invoice
from invoices.serializers import InvoiceSerializer

from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


# Allowing any user to access the view
@permission_classes((AllowAny, ))

# View for user interface
class InvoiceViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Invoice.objects.all() #Select Menu
    serializer_class = InvoiceSerializer #Serelize data


# Views for admin interface
class AllInvoicesView(LoginRequiredMixin, ListView):
    template_name = "admin_temp/invoice/invoices.html"
    model = Invoice
    ordering = ['-timestamp']
    paginate_by = 5

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('order')
