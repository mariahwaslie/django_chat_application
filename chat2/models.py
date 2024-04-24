from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import datetime
from django.utils.text import slugify
from django.urls import reverse


class Message(models.Model):
    sender= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)


class ChatGroup(models.Model):
    name = models.CharField(max_length=100,unique=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)
    description = models.TextField(max_length=250, blank=True,default=None)
    slug = models.SlugField(unique=True, allow_unicode=True,auto_created=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug =slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('chat2:single', kwargs={'slug':self.slug})

