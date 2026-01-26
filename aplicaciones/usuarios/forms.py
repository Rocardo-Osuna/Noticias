from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

Usuario = get_user_model()


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'tipo', 'nombre', 'apellidoP', 'apellidoM', 'edad' , 'foto')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
        

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'tipo', 'nombre', 'apellidoP', 'apellidoM', 'edad', 'foto')



class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'nombre', 'apellidoP', 'apellidoM' )

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario
    
        

    
        