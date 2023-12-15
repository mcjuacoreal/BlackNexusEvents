from django.db import models

# Create your models here.

class Evento(models.Model):

    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()
    telefono = models.CharField(max_length = 9)
    fecha_registro = models.DateField()
    titulo = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 600)
    fecha_realizacion = models.DateField()
    ubicacion = models.CharField(max_length = 50)
    realizado = models.BooleanField()

    def __str__(self):
        return self.titulo + " " + "(%s, %s)"%(self.nombre,self.fecha_realizacion)

