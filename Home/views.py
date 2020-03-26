from django.shortcuts import render


# Create your views here.
from account.forms import OrderForm
from account.models import Cars


def index(request):
    return render(request, 'Home/index.html')


def about(request):
    return render(request, 'Home/about.html')


def contact(request):
    return render(request, 'Home/contact.html')


def services(request):
    return render(request, 'Home/services.html')


def cars(request):
    car = Cars.objects.all()

    return render(request, 'Home/cars.html', {'car': car})


def bikes(request):
    return render(request, 'Home/bikes.html')


def index(request):
    car = Cars.objects.all()
    return render(request, 'Home/index.html', {'car': car})