from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from .models import ClientProfile, Cars, Bikes, Order
from .forms import RegisterForm, CustomerProfileForm, CarUploadForm, OrderForm, BikeUploadForm


# Create your views here.


def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request, 'account/login.html')


def customer_register(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = RegisterForm(request.POST)
        profile_form = CustomerProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/account/customer_login')
    else:
        form = RegisterForm(request.POST)
        profile_form = CustomerProfileForm(request.POST, request.FILES)
    return render(request, 'account/register.html', {'form': form, 'customer_profile_form':profile_form})


def customer_logout(request):
    auth.logout(request)
    return redirect('/')


def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('client_dashboard')
        else:
            return redirect('client_login')
    return render(request, 'account/client_login.html')

@login_required()
def client_dashboard(request):
    profile = request.user
    car = Cars.objects.filter(uploaded_by=profile)
    bike = Bikes.objects.filter(uploaded_by=profile)
    car_order = Order.objects.filter(car__in=car)
    bike_order = Order.objects.filter(bike__in=bike)

    return render(request, 'account/client_dashboard.html', {'car': car, 'bike': bike, 'car_order': car_order, 'bike_order': bike_order })


def client_logout(request):
    auth.logout(request)
    return redirect('/client_login/')


@login_required()
def upload_car(request):
    car = CarUploadForm
    if request.method == 'POST' or request.method=='FILES':
        car = CarUploadForm(request.POST, request.FILES)
        if car.is_valid():
            obj = car.save(commit=False)
            user = request.user
            obj.uploaded_by = user
            obj.save()
            return redirect('client_dashboard')
    return render(request, 'account/upload_car.html',{'car': car})


@login_required()
def upload_bike(request):
    bike = BikeUploadForm
    if request.method == 'POST' or request.method=='FILES':
        bike = BikeUploadForm(request.POST, request.FILES)
        if bike.is_valid():
            obj = bike.save(commit=False)
            user = request.user
            obj.uploaded_by = user
            obj.save()
            return redirect('client_dashboard')
    return render(request, 'account/bike_upload.html', {'bike': bike})


@login_required()
def rent_car(request, id):
    request.session.set_expiry(12000000)
    rent = OrderForm
    request.session['id'] = id
    the_id = request.session['id']
    car = Cars.objects.get(id=the_id)


    if request.method == 'POST':
        rent = OrderForm(request.POST)

        if rent.is_valid():
            obj = rent.save(commit=False)
            user = request.user
            obj.customer = user
            obj.car = car
            obj.save()
            return redirect('/')
    return render(request, 'account/order_form.html', {'form': rent, 'car':car})


@login_required()
def rent_bike(request, id):
    request.session.set_expiry(12000000)
    rent = OrderForm
    request.session['id'] = id
    the_id = request.session['id']
    bike = Bikes.objects.get(id=the_id)

    if request.method == 'POST':
        rent = OrderForm(request.POST)

        if rent.is_valid():
            obj = rent.save(commit=False)
            user = request.user
            obj.customer = user
            obj.bike = bike
            obj.save()
            return redirect('/')
    return render(request, 'account/order_form.html', {'form': rent})

def Carview(request):
    profile = request.user
    car = Cars.objects.filter(uploaded_by=profile)
    return render(request, 'account/car')