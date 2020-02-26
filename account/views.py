from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import login
from django.views.generic import CreateView


# Create your views here.

class Customer(CreateView):
    model = settings.AUTH_USER_MODEL


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
        return render(request, 'login.html')

        def customer_register(request):
            if request.method == 'POST':
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                user_name = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['pass']
                password2 = request.POST['repeat-pass']
                if password1 == password2:
                    if settings.AUTH_USER_MODEL.objects.filter(username=user_name).exists():
                        messages.info(request, 'username taken')
                        return redirect('register')
                    elif settings.AUTH_USER_MODEL.objects.filter(email=email).exists():
                        messages.info(request, 'email taken')
                        return redirect('account/register')
                    else:
                        user = settings.AUTH_USER_MODEL.objects.create_user(username=user_name, email=email, password=password1, first_name=first_name, last_name=last_name)
                        user.save()
                        return redirect('/')
                else:
                    return redirect('account/register')
            else:
                return render(request, 'register.html')

        def customer_logout(request):
            auth.logout(request)
            return redirect('/')


class Client(CreateView):
    def client_login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/client_dashboard')
            else:
                return redirect('login')
        return render(request, 'login.html')

    def client_dashboard(request):
        return render(request, 'client_dashboard.html')

    def client_logout(request):
        auth.logout(request)
        return redirect('/client_login/')