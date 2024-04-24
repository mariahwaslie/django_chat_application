from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
# Create your models here.
from django.db import models
from django.contrib import auth

class User(User,auth.models.PermissionsMixin):


    def __str__(self):
        #username is a built-in attribute from User
        return f'@{self.username}'
