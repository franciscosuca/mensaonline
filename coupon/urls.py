"""
4. Modify the urls

Import the the modules from DefaultRouter

"""

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'coupon', views.CouponViewSet)

app_name = 'coupon'

urlpatterns = [
    # routes for user pages
    path('', include(router.urls)),
]