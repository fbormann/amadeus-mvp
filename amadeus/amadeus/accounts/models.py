from django.db import models

# Create your models here.

import re
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('User', max_length=30,unique=True,validators=[
    validators.RegexValidator(
        re.compile('^[\w.@+-]+$'),
        'Informe um nome válido')])
    name = models.CharField('Name', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Staff', default=False) #If it can access admin site
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField('Entrance Date', auto_now_add=True)
    USERNAME_FIELD = 'username' #It's set that way so django knows which one
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
    	verbose_name='Usuário'
    	verbose_name_plural='Usuários'

    def __str__(self):
    	return self.name or self.username

    def get_full_name(self):
    	return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]



