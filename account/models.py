from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password = None):
        if not email:
            raise ValueError('user must have email')
        if not username:
            raise ValueError('user must have username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user


class ClientUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', unique=True)
    company_name = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    location = models.CharField(verbose_name='location', max_length=255)
    phone = models.BigIntegerField(verbose_name='phone')
    pan_vat = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name', 'location', 'phone', 'pan_vat']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj =None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True


class CustomerUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', unique=True)
    username = models.CharField(max_length=255, verbose_name='username', unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    location = models.CharField(verbose_name='location', max_length=255)
    phone = models.BigIntegerField(verbose_name='phone')
    license = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'location', 'phone', 'license']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True