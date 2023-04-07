
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('mostrar-fecha/', views.mostrar_fecha, name='mostrar_fecha'),
    path('saludar/', views.saludar, name='saludar'),
    path('mi-primer-plantilla/', views.mi_primer_plantilla, name='mi_primer_plantilla'),
    path('prueba-template/', views.prueba_template, name='prueba_template'),
    path('crear-animal/', views.crear_animal, name='crear_animal'),
    path('prueba-render/', views.prueba_render, name='prueba_render'),
    path('animales/', views.lista_animales, name='lista_animales'),
    
    
]
