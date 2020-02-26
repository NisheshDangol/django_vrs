from django.db import models
from django.conf import settings


# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    seat = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    available = models.BooleanField(default='True')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Bikes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    cc = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    available = models.BooleanField(default='True')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)