from django.shortcuts import render
from gestionEventos.models import Evento
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, "index.html")

def buscar_evento(request):
    return render(request,"buscar_eventos.html")

def programar_evento(request):
    return render(request,"programar_eventos.html")

def buscar(request):
    lugar = request.GET["lugar_evento"]
    eventos = Evento.objects.filter(ubicacion__icontains = lugar)
    return render(request, "resultado_busqueda.html",{"eventos": eventos,"lugar": lugar})

def agendar(request):
    if request.method == 'GET':
        # Obtener los datos del formulario
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido', '')
        email = request.GET.get('correo', '')
        telefono = request.GET.get('telefono', '')
        titulo = request.GET.get('titulo', '')
        fecha_pedido = request.GET.get('fecha_pedido', '')
        descripcion = request.GET.get('descripcion', '')
        ubicacion = request.GET.get('ubicacion', '')

        # Convertir fecha_pedido a formato de fecha
        try:
            fecha_realizacion = datetime.strptime(fecha_pedido, '%Y-%m-%d').date()
        except ValueError:
            # Manejo de error si la fecha no está en el formato correcto
            # Puedes ajustar esto según tus necesidades
            return render(request, 'error.html', {'mensaje': 'Fecha de pedido no válida'})

        # Crear una nueva instancia de Evento
        nuevo_evento = Evento(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            fecha_registro=datetime.now().date(),
            titulo=titulo,
            descripcion=descripcion,
            fecha_realizacion=fecha_realizacion,
            ubicacion=ubicacion,
            realizado=False
        )

        # Guardar la instancia en la base de datos
        nuevo_evento.save()
    return render(request,"gracias.html")
    