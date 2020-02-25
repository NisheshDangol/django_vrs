from django.urls import path
from .views import customer_login, customer_register, customer_logout, client_login, client_dashboard

urlpatterns = [
    path('login/', customer_login, name = 'customer_login'),
    path('register/', customer_register, name = 'customer_register'),
    path('logout/', customer_logout, name = 'customer_logout'),
    path('client_login/', client_login, name = 'client_login'),
    path('client_dashboard/', client_dashboard, name = 'client_dashboard')
]