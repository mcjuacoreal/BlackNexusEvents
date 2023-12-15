from django.contrib import admin
from gestionEventos.models import Evento

class EventosAdmin(admin.ModelAdmin):
    search_fields  = ("apellido","titulo","telefono","fecha_realizacion","fecha_registro","nombre") 
    list_filter = ("fecha_realizacion","ubicacion",)  
    date_hierarchy = "fecha_realizacion" 

admin.site.register(Evento,EventosAdmin)