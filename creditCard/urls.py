"""
4. Modify the urls

Import the the modules from DefaultRouter

"""

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'creditcard', views.CreditCardViewSet)

app_name = 'creditcard'

urlpatterns = [
    # routes for user pages
    path('', include(router.urls)),
]