from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Noticia
from django_ckeditor_5.widgets import CKEditor5Widget


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'portada', 'contenido', 'categorias', 'activo')
        widgets = {
            "contenido": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
            'categorias': Select2MultipleWidget(attrs={'style': 'width: 100%;'}),
          }
        error_messages = {
            'titulo': {
                'required': "El título es obligatorio.",
                'max_length': "El título no puede superar los 80 caracteres."
            },
            'portada': {
                'required': "Debes subir una imagen de portada."
            },
            'contenido': {
                'required': "El contenido no puede estar vacío."
            },
            'categorias': {
                'required': "Selecciona al menos una categoría."
            }
        }



