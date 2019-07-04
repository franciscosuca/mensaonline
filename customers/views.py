from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.contrib.auth.models import User
from . models import Customer

from customers.serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from django.contrib.auth.decorators import login_required
# from . forms import UserUpdateForm, CustomerUpdateForm
from . forms import CustomerUpdateForm

from django.views.generic import (
    ListView,
    # CreateView,
    UpdateView,
    DeleteView,
    #DetailView,
)


# Allowing any user to access the view
@permission_classes((AllowAny, ))

# View for user interface
class CustomerViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all() #Select Menu
    serializer_class = CustomerSerializer #Serelize data


# Views for admin interface
class AllCustomersView(LoginRequiredMixin, ListView):
    template_name = "admin_temp/user/customers.html"
    model = Customer
    paginate_by = 5

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set


@login_required
def updateCustomer(request, pk):
    customer   = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        c_form = CustomerUpdateForm(request.POST, request.FILES, instance=customer)

        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Customer Info has been Updated!')
            return redirect('customers:admin-customers')

    else:
        c_form = CustomerUpdateForm(instance=customer)    
  
    context = { 'c_form': c_form }

    return render(request, 'admin_temp/user/edit_customer.html', context) 

"""
class UpdateCustomerView(LoginRequiredMixin, UpdateView):
    template_name = "admin_temp/user/edit_customer.html"
    model = Customer
    fields = [
        'first_name', 'last_name', 'email_address', 'address', 'type', 'mobile'
    ]

    def form_valid(self, form):
        return super().form_valid(form)
"""

"""
@login_required
def updateCustomer(request, pk):
    u_customer = User.objects.get(pk=pk)
    customer   = Customer.objects.get(user_id=pk)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=u_customer)
        c_form = CustomerUpdateForm(request.POST, request.FILES, instance=customer)

        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            messages.success(request, f'Customer Info has been Updated!')
            return redirect('customers:admin-customers')

    else:
        u_form = UserUpdateForm(instance=u_customer)
        c_form = CustomerUpdateForm(instance=customer)    
  
    context = { 'u_form': u_form, 'c_form': c_form }

    return render(request, 'admin_temp/user/edit_customer.html', context)   
"""