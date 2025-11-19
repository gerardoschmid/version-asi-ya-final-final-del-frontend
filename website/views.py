
# website/views.py (Modificado)
from django.shortcuts import render

def index(request):
    # Ahora especificamos la ruta COMPLETA: 'nombre_de_la_app/nombre_del_archivo.html'
    return render(request, 'website/index.html')
# Puedes agregar más vistas aquí, por ejemplo, para la página "Nosotros"
def nosotros(request):
    """
    Renderiza la página "Nosotros".
    """
    # Usamos la ruta anidada
    return render(request, 'website/nosotros.html')

def acceso(request):
    """
    Renderiza la página de Acceso para administradores.
    """
    # Usamos la ruta anidada
    return render(request, 'website/acceso.html')

def habitaciones(request):
    """
    Renderiza la página de listado de habitaciones.
    """
    # Usamos la ruta anidada
    return render(request, 'website/habitaciones.html')

def reserva(request):
    """
    Renderiza el formulario de reserva de habitaciones.
    """
    return render(request, 'website/reserva_habitaciones.html')

def eventos(request):
    """
    Renderiza la página de salones y eventos.
    """
    return render(request, 'website/eventos.html') 

def reserva_eventos(request):
    """
    Renderiza el formulario de cotización/reserva de eventos.
    (Pendiente de HTML)
    """
    # Usaremos una plantilla simple de "en construcción" por ahora si no tienes el HTML
    return render(request, 'website/reserva_salon.html')

def detalle_habitacion(request, habitacion_id):
    """
    Renderiza la página de detalle de una habitación específica.
    En un proyecto real, se usaría habitacion_id para buscar datos.
    """
    # El ID se usa en el backend para buscar, pero lo pasamos aquí
    context = {'habitacion_id': habitacion_id} 
    return render(request, 'website/detalle_habitacion.html', context)
