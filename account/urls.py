from django.urls import path
from .views import customer_login, customer_logout, customer_register, client_login, client_dashboard, client_logout, \
    upload_car, rent_car, upload_bike

urlpatterns = [
    path('customer_login/', customer_login, name = 'customer_login'),
    path('customer_register/', customer_register, name = 'customer_register'),
    path('customer_logout/', customer_logout, name = 'customer_logout'),
    path('client_logout/', client_logout, name = 'customer_logout'),
    path('client_login/', client_login, name = 'client_login'),
    path('client_dashboard/', client_dashboard, name = 'client_dashboard'),
    path('upload_car/', upload_car, name = 'upload_car'),
    path('upload_bike/', upload_bike, name = 'upload_bike'),
    path('rent_car/<str:id>', rent_car, name = 'rent_car')
]