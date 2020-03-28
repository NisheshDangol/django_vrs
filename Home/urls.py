from django.urls import path
from .views import index, contact, services, cars, bikes


urlpatterns = [
    path('', index, name = 'index'),
    path('contact/', contact, name ='contact'),
    path('services/', services, name = 'services'),
    path('cars/', cars, name = 'cars'),
    path('bikes/', bikes, name = 'bikes'),
    path('cancel_booking/<str:id>', cancel_booking, name= 'cancel_booking')
]

