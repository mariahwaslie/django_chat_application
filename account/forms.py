from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

class RegisterForm(UserCreationForm):
    class Meta:
        #gives user acces to the folowing fields
        fields = ('username', 'email', 'password1', 'password2',)

        #gets the data for the current user
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'




