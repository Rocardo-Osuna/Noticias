from django.contrib import admin
from .models import Noticia, Categoria

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('id', 'titulo', 'autor__username', 'fecha', 'mostrar_categorias', 'activo', 'slug')
    list_filter = ('autor__username', 'activo')
    search_fields = ('titulo', 'autor__username',
                     'autor__nombre',
                     'autor__apellidoP',
                     'autor__apellidoM')
    date_hierarchy = 'fecha'
    ordering = ('autor__username',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ('categoria',)
    ordering = ('categoria',)