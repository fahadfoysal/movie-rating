from django import forms
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'release_date']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = CustomUser
        fields = fields = ['name', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
