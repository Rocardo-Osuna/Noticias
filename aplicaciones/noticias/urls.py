from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('noticia/<slug:slug>/', views.NoticiaDetailView.as_view(), name='ver_noticia'),
    path('prueba/', views.Prueba.as_view(), name='prueba'),
    path('crear-noticia', views.NoticiaCreateView.as_view(), name='crear-noticia'),
    path('editar-noticia/<int:pk>/', views.NoticiaUpdateView.as_view(), name='editar_noticia')
]