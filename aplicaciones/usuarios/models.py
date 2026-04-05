from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Usuario(AbstractUser):

    TIPO_USUARIOS = (
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('normal','Normal')
    )

    nombre = models.CharField(verbose_name='Nombre', null=True, blank=True, max_length=30)
    apellidoP = models.CharField(verbose_name='Apellido Paterno', null=True, blank=True, max_length=20)
    apellidoM = models.CharField(verbose_name='Apellido Materno', null=True, blank=True, max_length=20)
    mensaje = models.CharField(verbose_name='Algo sobre ti', null=True, blank=True, max_length=25)
    tipo = models.CharField(choices=TIPO_USUARIOS, default='normal', max_length=20)
    foto = models.ImageField(upload_to='imagenes_perfil', blank=True, null=True)
    edad = models.PositiveIntegerField(verbose_name='edad', null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.username} - {self.nombre or ""} {self.apellidoP or ""} {self.apellidoM or ""}'
    
    #Esto solo lo agregue como practica, puede eliminarse sin problema
    def clean(self):
        if self.edad is not None:
            if self.edad > 120:
                raise ValidationError({'edad': 'Dudo que seas tan viejo'})
            elif self.edad < 6:
                raise ValidationError({'edad': 'Que haces en esta pagina, eres muy niño'})
        
    def save(self, *args, **kwargs ):
        self.full_clean()
        return super().save()     



