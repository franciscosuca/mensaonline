"""mensa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users import views as my_user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin-menu/', include('menus.urls')),

    path('registration/', my_user_views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='admin_temp/user/login.html'), name='login'),
    path('profile/', my_user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='admin_temp/user/logout.html'), name='logout'),
    
    # code for django-vue integration
    # path('', TemplateView.as_view(template_name='index.html')),
    path('notes/',include('testApp.urls')),
    path('customer/', include('customers.urls')),
    path('menu/',include('menus.urls')),
    path('orders/',include('orders.urls')),
    path('invoice/',include('invoices.urls')),
    path('wallet/',include('wallets.urls')),
    path('coupon/',include('coupon.urls')),
    path('creditcard/',include('creditCard.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
