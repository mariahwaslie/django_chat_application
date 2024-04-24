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


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=50, unique=True)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     def __str__(self):
#         return f'@{self.username}'