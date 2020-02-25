from django.urls import path
from .views import index, about, contact, services, cars, bikes


urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name ='contact'),
    path('services/', services, name = 'services'),
    path('cars/', cars, name = 'cars'),
    path('bikes/', bikes, name = 'bikes')
]

