from django.http import HttpResponse    
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Animal
from django.shortcuts import render, redirect
from inicio.forms import CreacionAnimalFormulario, BuscarAnimal

def mi_vista(request):
    return render(request, r'inicio/index.html')

'''Version con http response'''
# def mostrar_fecha(request):
#     dt = datetime.now()
#     dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
#     return HttpResponse(f'<p>{dt_formateado}</p>')

def saludar(request):
    return HttpResponse('<h1>Hola Ricardo Diaz</h1>')

"""Este formato es pasandole el la ruta del archivo desde mi compu"""
def mi_primer_plantilla(request):
    archivo = open(r'C:\Users\Rdiaz\OneDrive\RICARDO DIAZ\CURSO PYTHON\CODERHOUSE\CLASES\DJANGO\proyecto-django\templates\mi_primer_plantilla.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)



'''Version nueva con template'''

"""Este formato es ya pasandole las rutas de los archivos para que empiecen
a interactuar con el proyecto entre si llendome al archivo de 
settings.py  y en

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        
        """
def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    
    template = loader.get_template(r'inicio/mostrar_fecha.html')
    template_renderizado = template.render({'fecha': dt_formateado})
    return HttpResponse(template_renderizado)
    
#====================================================================    
def prueba_template(request):
    datos = {
        'nombre': 'Ricardo',
        'Apellido': 'Diaz',
        'edad': 25,
        'años':  [1995, 2004, 2014, 2017, 2021, 2022]
    }
    
    template = loader.get_template(r'inicio/prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

#===================================================================
#Ejemplo 1
# def crear_animal(request):
#     animal = Animal(nombre= 'Toncha 2', edad= 3)
#     print(animal.nombre)
#     print(animal.edad)
#     animal.save()
#     datos={'animal': animal}
#     template = loader.get_template(r'inicio/crear_animal.html')
#     template_renderizado = template.render(datos)
#     return HttpResponse(template_renderizado)

#Ejemplo 2
# def crear_animal(request):
#     if request.method == "POST":
#         animal = Animal(nombre= request.POST['nombre'], edad= request.POST['edad'])
#         animal.save()
#     return render(request, 'inicio/crear_animal_ej2.html')

#Ejemplo 3
def crear_animal(request):
    if request.method == "POST":
        formulario = CreacionAnimalFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            animal = Animal(nombre= datos_correctos['nombre'], edad= datos_correctos['edad'])
            animal.save()
            
            return redirect('inicio:lista_animales')
            
    formulario = CreacionAnimalFormulario()
    return render(request, 'inicio/crear_animal_ej3.html', {'formulario': formulario})
#===================================================================

def lista_animales(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        animales = Animal.objects.filter(nombre__icontains=nombre_a_buscar)
    else:    
        animales = Animal.objects.all()
    formulario_busqueda = BuscarAnimal()
    return render(request, 'inicio/lista_animales.html', {'animales': animales, 'formulario': formulario_busqueda})
    

#===================================================================
'''Esta es una nueva forma de hacer una nueva vista
Para hacer esta vista es importante hacer la siguiente importacion

from django.shortcuts import render

'''
def prueba_render(request):
    datos = {'nombre': 'ricardo'}
        
    '''Por convencion siempre se tiene que poner como primer 
    argumento request, despues la ruta del template y despues
    el dato que va a jalar'''
    
    return render(request, r'inicio/prueba_render.html', datos)