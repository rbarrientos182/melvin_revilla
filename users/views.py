from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/register.html"

def error_500(request):
    context = {"message": "Usuario creado correctamente"}
    return render(request, '500.html', context)

def error_401(request):
    context = {"message": "Usuario creado correctamente"}
    return render(request, '401.html', context)

def error_404(request):
    context = {"message": "Usuario creado correctamente"}
    return render(request, '404.html', context)