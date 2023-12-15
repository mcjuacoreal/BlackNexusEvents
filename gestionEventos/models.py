from django.db import models

"""
Clase representadno un evento.
Hereda de la clase models.Model

Está conectada con la base de datos "gestionEventos".
Cualquier intancia de la clase que sea guardada será subida a la base de datos y será visible desde la 
página.
"""
class Evento(models.Model):

    #Nombre de quien reserva
    nombre = models.CharField(max_length = 20)  
    #Apeliido de quien reserva
    apellido = models.CharField(max_length = 30)  
    #Email de quien reserva  
    email = models.EmailField() 
    #Telefono de quien reserva
    telefono = models.CharField(max_length = 9)
    #Fecha de inscripcion del evento
    fecha_registro = models.DateField()
    titulo = models.CharField(max_length = 30)
    #Titulo del evento
    descripcion = models.CharField(max_length = 600)
    #Fecha de realizacion del evento
    fecha_realizacion = models.DateField()
    #Ubicacion del evento
    ubicacion = models.CharField(max_length = 50)
    #Booleano indicando si el evento fue realizado o no
    realizado = models.BooleanField()

    #Forma de string de la tupla, solo muestra el titulo, el nombre de quien reservo y la fecha de 
    #realización, que son los atributos clave (Esto solo es visible desde el panel de administración).
    def __str__(self):
        return self.titulo + " " + "(%s, %s)"%(self.nombre,self.fecha_realizacion)

