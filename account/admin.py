from django.contrib import admin
from . models import ClientProfile,CustomerProfile,User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(User)
admin.site.register(ClientProfile)
admin.site.register(CustomerProfile)