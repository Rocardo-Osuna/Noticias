from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import PROTECT
from django.utils.text import slugify
 
from django_ckeditor_5.fields import CKEditor5Field

Usuario = get_user_model()


class Categoria(models.Model):
    categoria = models.CharField(verbose_name='Categoria', blank=False, null=False, max_length=20)

    class Meta:
        verbose_name = 'Cateogoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria
    

class Noticia(models.Model):
    titulo = models.CharField(verbose_name='Titulo', null=False, blank=False, max_length=80)
    portada = models.ImageField(upload_to='portadas')
    contenido = CKEditor5Field('Text', config_name='extends')
    categorias = models.ManyToManyField(Categoria, related_name='noticias')
    activo = models.BooleanField(default=False)
    autor = models.ForeignKey(Usuario, on_delete=PROTECT, related_name='noticias')
    slug = models.SlugField(unique=True , blank=True)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)
            slug = base
            contador = 1
            while Noticia.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{contador}"
                contador += 1
            self.slug = slug
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.titulo} - {self.autor.username}'
    
    def mostrar_categorias(self):
        return ", ".join([c.categoria for c in self.categorias.all()])
      
    mostrar_categorias.short_description = "Categorías"


