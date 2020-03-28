from django.urls import path
from .views import customer_login, customer_logout, customer_register, client_login, client_dashboard, client_logout, \
    upload_car, rent_car, upload_bike, carview, bikeview, edit_car, delete_car, delete_bike, edit_bike, rent_bike, \
    confirm_booking, delete_booking

urlpatterns = [
    path('customer_login/', customer_login, name = 'customer_login'),
    path('customer_register/', customer_register, name = 'customer_register'),
    path('customer_logout/', customer_logout, name = 'customer_logout'),
    path('client_logout/', client_logout, name = 'customer_logout'),
    path('client_login/', client_login, name = 'client_login'),
    path('client_dashboard/', client_dashboard, name = 'client_dashboard'),
    path('upload_car/', upload_car, name = 'upload_car'),
    path('upload_bike/', upload_bike, name = 'upload_bike'),
    path('rent_car/<str:id>', rent_car, name = 'rent_car'),
    path('rent_bike/<str:id>', rent_bike, name = 'rent_bike'),
    path('car_list/', carview, name = 'car_list'),
    path('bike_list/', bikeview, name = 'bike_list'),
    path('car_edit/<str:id>', edit_car, name = 'car_edit'),
    path('bike_edit/<str:pk>', edit_bike, name = 'bike_edit'),
    path('car_delete/<str:id>', delete_car, name='car_delete'),
    path('bike_delete/<str:id>', delete_bike, name='bike_delete'),
    path('confirm_booking/<str:id>', confirm_booking, name='confirm_booking'),
    path('delete_booking/<str:id>', delete_booking, name='delete_booking'),
]