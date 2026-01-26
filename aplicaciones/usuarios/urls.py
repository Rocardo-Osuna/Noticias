from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'usuario'

urlpatterns = [
    #path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', views.UsuarioCreateView.as_view(), name='registrar')
    #path('crear-usuario/', views.prueba, name='crear_usuario')
]