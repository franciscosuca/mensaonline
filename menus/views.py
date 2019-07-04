"""
3. Modify the view

Import the the modules from rest_framework to call viewsets
Import the the modules from rest_framework.permissions to call modules for auth
Import the class from serializer file

"""

from menus.models import Menu
from menus.serializers import MenuSerializer
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    #DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

# Allowing any user to access the view
@permission_classes((AllowAny, ))


# View for user interface
class MenuViewSet(viewsets.ModelViewSet):
    today = date.today()

    permission_classes = (IsAuthenticated,)
    queryset = Menu.objects.all() #Select Menu
    # queryset = Menu.objects.filter(day__year=today.year,
    #                            day__month=today.month,
    #                            day__day=today.day)
    serializer_class = MenuSerializer #Serelize data


# Views for admin interface
class MenuView(LoginRequiredMixin, ListView):
    template_name = "admin_temp/menu/menu.html"
    model = Menu
    ordering = ['-update']
    paginate_by = 4

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set


class AddMenuView(LoginRequiredMixin, CreateView):
    template_name = "admin_temp/menu/menu_form.html"
    model = Menu
    
    fields = [
        'title', 'description', 'category', 'status', 'calories',
        'price_student', 'price_guest', 'price_attendant',
        'day', 'slug', 'quantity', 
    ]

    def form_valid(self, form):
        #messages.success(request, f'A Food item is added!')
        #form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateMenuView(LoginRequiredMixin, UpdateView):
    template_name = "admin_temp/menu/menu_form.html"
    model = Menu
    fields = [
        'title', 'description', 'category', 'status', 'calories',
        'price_student', 'price_guest', 'price_attendant',
        'day', 'slug', 'quantity', 
    ]

    def form_valid(self, form):
        #messages.success(request, f'A Food item is added!')
        return super().form_valid(form)


class DeleteMenuView(LoginRequiredMixin, DeleteView):
    template_name = "admin_temp/menu/menu_confirm_delete.html"
    model = Menu
    success_url = '/menu/admin-menu/'