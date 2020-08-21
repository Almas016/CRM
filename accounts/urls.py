from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('customer/<str:pk_test>', views.customer),
    path('product/', views.products),
]