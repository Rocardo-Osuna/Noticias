from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, login, authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UsuarioForm
from django.views.generic import CreateView
import random

Usuario = get_user_model()


class RolMixin:
    def dispatch(self, request, *args, **kwargs):
        tipo_usuario = request.user.tipo

        if isinstance(self.tipo_requerido, str):
            if tipo_usuario != self.tipo_requerido:
                return redirect(reverse_lazy('inicio'))
        
        if isinstance(self.tipo_requerido, (list,tuple)):
            if tipo_usuario not in self.tipo_requerido:
                return redirect(reverse_lazy('inicio'))
            
        return super().dispatch(request, *args, **kwargs)

    
class Login(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or reverse_lazy('inicio')

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrecto')

        form.add_error('username', 'El usuario no existe')
        form.add_error('password', 'La contraseña no es correcta')

        return super().form_invalid(form)



class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('inicio')
    template_name = "registro.html"

    def get_success_url(self):
        return self.request.GET.get('next') or reverse_lazy('inicio')

    def form_valid(self, form):
        usuario = super().form_valid(form)
        login(self.request, self.object)
            
        return usuario






