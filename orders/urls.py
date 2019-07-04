
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


# Code to call REST API views 

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)

app_name = 'orders'

urlpatterns = [
    
    path('', include(router.urls)),

    path('admin-orders/', views.AllOrdersView.as_view(), name="admin-orders"),
    path('admin-orders/<int:pk>/accept/', views.acctept_or_deny, name="order-action"),
]