from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

from account.models import Cars, Bikes, Order, CustomerProfile


def index(request):
    car = Cars.objects.all()
    bike = Bikes.objects.all()
    return render(request, 'Home/index.html', {'car':car, 'bike':bike})


def contact(request):
    return render(request, 'Home/contact.html')


def services(request):
    return render(request, 'Home/services.html')


def cars(request):
    car = Cars.objects.all()

    return render(request, 'Home/cars.html', {'car': car})


def bikes(request):
    bike = Bikes.objects.all()
    return render(request, 'Home/bikes.html', {'bike':bike})


def index(request):
    car = Cars.objects.all()
    return render(request, 'Home/index.html', {'car': car})


@login_required()
def booking_detail(request):
    order=Order.objects.filter(customer=request.user)
    return render(request, 'Home/booking_detail.html', {'order':order})



@login_required()
def cancel_booking(request,id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        if order.status == 'Pending':
            order.status = "Canceled"
            order.save()
        return redirect('booking_detail_home')
    return render(request, 'Home/cancel_booking.html', {'order':order})
