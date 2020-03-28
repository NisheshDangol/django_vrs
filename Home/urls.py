from django.urls import path
from .views import index, contact, services, cars, bikes, booking_detail, cancel_booking

urlpatterns = [
    path('', index, name = 'index'),
    path('contact/', contact, name ='contact'),
    path('services/', services, name = 'services'),
    path('cars/', cars, name = 'cars'),
    path('bikes/', bikes, name = 'bikes'),
    path('booking_detail/', booking_detail, name= 'booking_detail_home'),
    path('cancel_booking/<str:id>', cancel_booking, name= 'cancel_booking'),

]

