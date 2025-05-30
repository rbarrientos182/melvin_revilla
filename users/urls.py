from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, error_500, error_401, error_404

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("error_500/", error_500, name="error_500"),
    path("error_401/", error_401, name="error_401"),
    path("error_404/", error_404, name="error_404"),

]