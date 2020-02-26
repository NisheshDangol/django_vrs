from django.urls import path
from .views import Client,Customer

urlpatterns = [
    path('customer_login/', Customer.customer_login, name = 'customer_login'),
    path('customer_register/', Customer.customer_register, name = 'customer_register'),
    path('logout/', Customer.customer_logout, name = 'customer_logout'),
    path('client_logout/', Client.client_logout, name = 'customer_logout'),
    path('client_login/', Client.client_login, name = 'client_login'),
    path('client_dashboard/', Client.client_dashboard, name = 'client_dashboard')
]