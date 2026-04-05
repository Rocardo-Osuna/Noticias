from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('noticia/<slug:slug>/', views.NoticiaDetailView.as_view(), name='ver_noticia'),
    path('crear-noticia', views.NoticiaCreateView.as_view(), name='crear-noticia'),
    path('editar-noticia/<int:pk>/', views.NoticiaUpdateView.as_view(), name='editar_noticia'),
    path('noticias-editor/', views.NoticiasEditorListView.as_view(), name="noticias_editor")
]