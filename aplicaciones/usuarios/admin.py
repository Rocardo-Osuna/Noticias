from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UsuarioForm, UsuarioChangeForm
from django.contrib.auth.admin import UserAdmin

Usuario = get_user_model()

@admin.register(Usuario)
class Admin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioForm

    list_display = ('username', 'nombre', 'apellidoP', 'apellidoM','tipo', 'date_joined')
    list_filter = ('is_active', 'tipo')
    search_fields = ('username', 'nombre', 'apellidoP', 'apellidoM')
    ordering = ('username',)

    fieldsets = (					
        (None, {'fields': ('username', 'password', 'tipo', 'nombre', 'apellidoP', 'apellidoM', 'edad' , 'foto')}),
        ('Información personal', {'fields': ('email',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'tipo',  'nombre', 'apellidoP', 'apellidoM', 'edad', 'email', 'foto', 'is_active', 'is_staff'),
        }),
    )
