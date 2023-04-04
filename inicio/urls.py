
from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.mi_vista),
    path('mostrar-fecha/', views.mostrar_fecha),
    path('saludar/', views.saludar),
    path('mi-primer-plantilla/', views.mi_primer_plantilla),
    path('prueba-template/', views.prueba_template),
    path('crear-animal/', views.crear_animal),
    
]
