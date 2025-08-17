from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ContactFormForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    flanes = Producto.objects.all()
    return render(request, "web/home.html", {"flanes": flanes})


@login_required
def home_premium(request):
    return render(request, "web/home_premium.html", {})

def contacto(request):
    mensaje_enviado = False
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")
        # Aquí puedes guardar en la base de datos o enviar email
        mensaje_enviado = True
    return render(request, "web/contacto.html", {"mensaje_enviado": mensaje_enviado})
