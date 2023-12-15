from django.contrib import admin
from gestionEventos.models import Evento

# Configuración de panel de control de eventos
class EventosAdmin(admin.ModelAdmin):
    # Formas de buscar un evento
    search_fields  = ("apellido","titulo","telefono","fecha_realizacion","fecha_registro","nombre") 
    # Filtros para el panel de administración
    list_filter = ("fecha_realizacion","ubicacion",)  
    # Menú de miga para busqueda de fecha
    date_hierarchy = "fecha_realizacion" 

#Registro de la clase evento junto con su configuración en el panel de administración
admin.site.register(Evento,EventosAdmin)