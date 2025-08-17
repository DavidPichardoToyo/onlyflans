from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Registro, LoginView, LogoutView

urlpatterns = [
    path("registro/", Registro.as_view(), name="registro"),
   path("login/",  auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
