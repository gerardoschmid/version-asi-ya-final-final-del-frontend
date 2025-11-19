# website/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mapea la ruta raíz ('') a la función views.index 
    path('', views.index, name='home'), 
    # Mapea la ruta 'nosotros/' a la función views.nosotros
    path('nosotros/', views.nosotros, name='nosotros'),

    path('acceso/', views.acceso, name='acceso'),

    path('habitaciones/', views.habitaciones, name='habitaciones'),

    path('reservar/', views.reserva, name='reserva'),

    path('eventos/', views.eventos, name='eventos'),
    path('cotizar-evento/', views.reserva_eventos, name='reserva_eventos'),

    path('habitaciones/<int:habitacion_id>/', views.detalle_habitacion, name='detalle_habitacion'),
]