import uuid
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField("Producto", max_length=50)
    descripcion = models.TextField("Descripcion")
    precio = models.DecimalField("Precio", max_digits=5, decimal_places=0)
    stock = models.PositiveIntegerField("Stock", default=0)
    imagen = models.ImageField("Imagen", upload_to="productos/")



class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


def __str__(self):
    return self.nombre_producto