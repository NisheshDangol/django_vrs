from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.
from django.utils.text import slugify


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=255)
    licence = models.ImageField(upload_to='pics')
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.is_customer = True
        super().save(*args, **kwargs)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=255)
    pan_vat = models.ImageField()
    is_client = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_client = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Cars(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    seat = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    available = models.BooleanField(default='True')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bikes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    cc = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    available = models.BooleanField(default='True')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Canceled', 'Canceled'),
        ('Pending', 'Pending')
    ]
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, null=True, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bikes, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=256)
    date_of_delivery = models.DateField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='Pending', choices=STATUS)
    return_date = models.DateTimeField()
    no_of_vehicle = models.IntegerField(default=1)

    def __unicode__(self):
        return self.car.name

    def __str__(self):
        if self.car:
            return self.car.name
        else:
            return self.bike.name
