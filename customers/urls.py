from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

# Code to call REST API views 

router = DefaultRouter()
router.register(r'customer', views.CustomerViewSet)

app_name = 'customers'
urlpatterns = [
    # routes for user pages
    path('', include(router.urls)),

    # routes for admin pages
    path('admin-customers/', views.AllCustomersView.as_view(), name="admin-customers"),
    # path('admin-customers/<int:pk>/update/', views.UpdateCustomerView.as_view(), name="customer-update"),
    
    path('admin-customers/<int:pk>/update/', views.updateCustomer, name="customer-update"),
    
]