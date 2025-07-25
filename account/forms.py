from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)