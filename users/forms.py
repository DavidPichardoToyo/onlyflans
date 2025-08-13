from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class FormularioRegistro(UserCreationForm):
    class meta:
        model = User
        field = ('username', 'password 1', 'password 2')