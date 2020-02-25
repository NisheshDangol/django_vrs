from django.shortcuts import render
from .models import Cars

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def cars(request):
    car = Cars.objects.all()
    return render(request, 'cars.html', {'car': car})


def bikes(request):
    return render(request, 'bikes.html')


def index(request):
    car = Cars.objects.all()
    return render(request, 'index.html', {'car': car})