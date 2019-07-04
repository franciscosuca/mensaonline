from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'invoice', views.InvoiceViewSet)

app_name = 'invoices'

urlpatterns = [
    # routes for user pages
    path('', include(router.urls)),

    # routes for admin pages
    path('admin-invoices', views.AllInvoicesView.as_view(), name="admin-invoices"),
]