from accounts.managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('nombre'), max_length=70)
    email = models.EmailField(_('correo'), unique=True)
    username = models.CharField(_('nombre de usuario'), unique=True, max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','email']

    objects = CustomUserManager()