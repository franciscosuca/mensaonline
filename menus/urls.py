"""
4. Modify urls

import default rourter to call django rest framework interface
import  views from the app
import modules to use path and include methods
"""

from rest_framework.routers import DefaultRouter
from menus import views
from django.urls import path, include

#from rest_framework import routers

# Code to call REST API views 

#router = routers.SimpleRouter()
router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    # routes for user pages
    path('', include(router.urls)),

    # routes for admin pages
    path('admin-menu/', views.MenuView.as_view(), name="admin-menu"),
    path('admin-menu/new/', views.AddMenuView.as_view(), name="menu-create"),
    path('admin-menu/<int:pk>/update/', views.UpdateMenuView.as_view(), name="menu-update"),
    path('admin-menu/<int:pk>/delete/', views.DeleteMenuView.as_view(), name="menu-delete"),
]

# Code to call admin views 

# app_name = 'menus'
# urlpatterns = [
#     path('', views.MenuView.as_view(), name="menu"),
    
    # path('add-menu/', views.AddMenuView.as_view(), name="add-menu"),
# ]

