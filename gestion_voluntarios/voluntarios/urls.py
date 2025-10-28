from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    #URLS para los voluntarios
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('voluntarios/nuevo/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntarios/<int:pk>/editar/', views.editar_voluntario, name='editar_voluntario'),
    path('voluntarios/<int:pk>/eliminar/', views.eliminar_voluntario, name='eliminar_voluntario'),
    
    # URLS para los eventos
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/nuevo/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:pk>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
]