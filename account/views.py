from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RegisterForm
from braces.views import SelectRelatedMixin
from django.contrib.auth.views import LoginView, auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
class RegisterView(SelectRelatedMixin, CreateView):

    form_class = RegisterForm
    success_url = reverse_lazy('home')
    template_name = 'account/register.html'

class LoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('account/profile')

class ProfileView(LoginRequiredMixin,View):

    def get(self, request):
        return render(request, 'account/profile.html')
