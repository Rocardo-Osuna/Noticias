from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404 
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.views import View
from .models import Noticia
from .forms import NoticiaForm
from aplicaciones.usuarios.views import RolMixin



class InicioListView(ListView):
    model = Noticia
    context_object_name = "noticias"
    template_name = "noticias/index.html"

    def get_queryset(self):
        return self.model.objects.filter(activo=True).order_by('-fecha', '-id')





class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "noticias/ver_noticia.html"
    context_object_name = 'noticia'
    slug_field = 'slug'        
    slug_url_kwarg = 'slug'


class NoticiaCreateView(LoginRequiredMixin, RolMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "noticias/crear_noticia.html"
    success_url = reverse_lazy('inicio')
    tipo_requerido = 'editor'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

class NoticiaUpdateView(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "noticias/crear_noticia.html"
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.autor != self.request.user:
            raise Http404("No tienes permiso para editar esta noticia.")
        return obj
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    

class NoticiasEditorListView(LoginRequiredMixin, RolMixin, ListView):
    model = Noticia
    context_object_name = "noticias"
    template_name = "noticias/noticias_editor.html"
    tipo_requerido = 'editor'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user).order_by('-fecha', '-id')


class EliminarNoticia(LoginRequiredMixin, RolMixin):
    model = Noticia
    tipo_requerido = 'editor'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user)

    
class RestaurarNoticia(LoginRequiredMixin, RolMixin):
    model = Noticia
    tipo_requerido = 'editor'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user)

