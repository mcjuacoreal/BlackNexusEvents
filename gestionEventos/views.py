from django.shortcuts import render
from gestionEventos.models import Evento
from datetime import datetime
# Create your views here.

#Vista de la página principal
def index(request):
    return render(request, "index.html")

#Vista de la página de busqueda de eventos
def buscar_evento(request):
    return render(request,"buscar_eventos.html")

#Vista de la página de programación de eventos
def programar_evento(request):
    return render(request,"programar_eventos.html")

#Vista del resultado de la busqueda de eventos
def buscar(request):
    #Se recupera lo ingresado en el formulario vía GET
    lugar = request.GET["lugar_evento"]
    #Se busca en la base de datos
    eventos = Evento.objects.filter(ubicacion__icontains = lugar)
    #Se entrega a resultado_busqueda.html junto con el contexto correspondiente
    return render(request, "resultado_busqueda.html",{"eventos": eventos,"lugar": lugar})

#Vista del resultado de agendar un evento nuevo
def agendar(request):
    if request.method == 'GET':
        # Se obtienen los datos del formulario vía GET
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido', '')
        email = request.GET.get('correo', '')
        telefono = request.GET.get('telefono', '')
        titulo = request.GET.get('titulo', '')
        fecha_pedido = request.GET.get('fecha_pedido', '')
        descripcion = request.GET.get('descripcion', '')
        ubicacion = request.GET.get('ubicacion', '')

        # Se convierte fecha_pedido a formato de fecha
        fecha_realizacion = datetime.strptime(fecha_pedido, '%Y-%m-%d').date()

        # Se crea una nueva instancia de Evento
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

        # Se guarda la instancia en la base de datos
        nuevo_evento.save()
    return render(request,"gracias.html")
    