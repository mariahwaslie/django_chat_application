# chat/views.py
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView,TemplateView
from .models import *
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime,timezone
from .forms import GroupForm
from .models import ChatGroup
from django.views import generic




class CreateChatGroup(CreateView, LoginRequiredMixin):
    model=ChatGroup
    template_name = 'chat/create_group.html'
    fields = ('name', 'description')
    #change to  the groups page
    success_url = reverse_lazy('home')

class JoinChatGroup(ListView,LoginRequiredMixin):
    model = ChatGroup
    template_name = "chat/join_group.html"
    context_object_name = 'groups'
    # extra_context = {'groups':ChatGroup.objects.all()}
    #
    # def get(self, request, *args, **kwargs):
    #     groups = get_object_or_404(ChatGroup,slug=self.kwargs.get("slug"))
    #
    #     # try:
    #     #     ChatGroup.objects.create(user=self.request.user,group=group)
    #     return super().get(request, *args, **kwargs)


def index(request):
    return render(request, "chat/index.html")

@login_required(login_url='login')
def room(request, room_name):
    username = request.user.username
    return render(request, "chat/room.html", {"room_name": room_name,
                                              "username": username})




