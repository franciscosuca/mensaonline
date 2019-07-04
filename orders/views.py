from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from . models import Order
from orders.serializers import OrderSerializer

from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

# Allowing any user to access the view
@permission_classes((AllowAny, ))

# View for user interface
class OrderViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all() #Select Menu
    serializer_class = OrderSerializer #Serelize data


# View for Admin
class AllOrdersView(LoginRequiredMixin, ListView):
    template_name = "admin_temp/order/orders.html"
    model = Order
    ordering = ['-timestamp']
    paginate_by = 4

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('customer')


def acctept_or_deny(request, pk):
    orderAction = Order.objects.get(pk=pk)
    if request.POST['action'] == "Approve":
        orderAction.status = "Aproved"

    elif request.POST['action'] == "Cancel":
        orderAction.status = "Canceled"    
    
    orderAction.save()
    
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('orders:admin-orders'))    
