from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:   # <- con M mayúscula
        model = User
        fields = ("username", "email", "password1", "password2")


