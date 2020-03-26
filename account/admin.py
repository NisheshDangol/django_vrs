from django.contrib import admin
from .models import ClientProfile, CustomerProfile, Cars, Bikes, Order

from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(ClientProfile)
admin.site.register(CustomerProfile)
admin.site.register(Cars)
admin.site.register(Bikes)
admin.site.register(Order)