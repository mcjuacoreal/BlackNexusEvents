from django.test import TestCase
from gestionEventos.models import Evento
from datetime import *

evento = Evento(
        nombre="Joaquin",
        apellido="Figueroa",
        email="jo.figueroa.mora@gmail.com",
        telefono="975211349",
        fecha_registro=datetime.now().date(),
        titulo="Gala octavo basico",
        descripcion="Gala para 42 niños de 14 años, debe haber buffet, parlantes para musica y coctel para los apoderados",        
        fecha_realizacion=2024-12-22,
        ubicacion="Ballenar",
        realizado=False
        )