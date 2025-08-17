from django.urls import path
from .views import home, home_premium, contacto

urlpatterns = [
   path("home/", home, name="home" ),
   path("premium/", home_premium, name="home_premium"),
   path("contacto/", contacto, name="contacto")
]
