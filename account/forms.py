from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CustomerProfile, Bikes
from .models import Cars, Order


class CustomerProfileForm(forms.ModelForm):
    is_customer = forms.BooleanField
    phone = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'phone number'}))
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'location'}))
    licence = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'input', 'required': True, 'placeholder': 'licence'}))
    class Meta:
        model = CustomerProfile
        fields = [
            'location',
            'phone',
            'licence',
        ]


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Repeat Password'}))


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input100', 'required': True, 'placeholder': 'Repeat Password'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CarUploadForm(forms.ModelForm):
    name = forms.TextInput()
    price = forms.NumberInput()
    seat = forms.NumberInput()
    desc = forms.Textarea()
    img = forms.FileInput()
    available = forms.CheckboxInput()
    class Meta:
        model = Cars
        fields =[
            'name',
            'price',
            'seat',
            'desc',
            'img',
            'available'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Price'}),
            'seat': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Seat'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Description'}),
            'img': forms.FileInput(attrs={'class': 'form-control-file', 'required': True, 'placeholder': 'Image'}),
        }


class BikeUploadForm(forms.ModelForm):
    name = forms.TextInput()
    price = forms.NumberInput()
    cc = forms.NumberInput()
    desc = forms.Textarea()
    img = forms.FileInput()
    available = forms.CheckboxInput()
    class Meta:
        model = Bikes
        fields =[
            'name',
            'price',
            'cc',
            'desc',
            'img',
            'available'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Price'}),
            'cc': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'CCs'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Description'}),
            'img': forms.FileInput(attrs={'class': 'form-control-file', 'required': True, 'placeholder': 'Image'}),
        }


class OrderForm(forms.ModelForm):
    location = forms.TextInput()
    date_of_delivery = forms.DateInput()
    return_date = forms.DateTimeInput()
    no_of_vehicle = forms.IntegerField()
    class Meta:
        model = Order
        fields = [
            'location',
            'date_of_delivery',
            'return_date',
            'no_of_vehicle',
        ]


