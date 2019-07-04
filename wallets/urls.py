"""
4. Modify the urls

Import the the modules from DefaultRouter

"""

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wallet', views.WalletViewSet)

app_name = 'wallets'

urlpatterns = [
    # routes for user pages
    path('', include(router.urls)),

    # routes for admin pages
    # path('admin-wallets', views.AllInvoicesView.as_view(), name="admin-wallets"),
]