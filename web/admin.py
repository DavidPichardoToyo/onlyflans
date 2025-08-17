from django.contrib import admin
from .models import Producto, ContactForm

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactForm)
class FormularioContacto(admin.ModelAdmin):
    pass