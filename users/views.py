from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import FormularioRegistro
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView




# Create your views here.
class Registro(SuccessMessageMixin, CreateView):
    form_class = FormularioRegistro
    template_name = "users/registro.html"
    success_url = reverse_lazy("login")
    success_message = "Registro exitoso"


class Login(LoginView):
    template_name = "users/login.html"

class Logout(LogoutView):
    next_page = reverse_lazy("home")
    http_method_names = ["get", "post"]


def registro_view(request):
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # redirige al login después de registrar
    else:
        form = FormularioRegistro()
    
    return render(request, "web/registro.html", {"form": form})

    