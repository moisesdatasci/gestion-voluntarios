from django.contrib import admin
from .models import Voluntario, Evento

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'fecha_registro']
    search_fields = ['nombre', 'email']
    list_filter = ['fecha_registro']

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    search_fields = ['titulo', 'descripcion']
    list_filter = ['fecha']
    filter_horizontal = ['voluntarios']