from django.http import HttpResponse    
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Animal

def mi_vista(request):
    return HttpResponse('<h1>Mi primera Vista</h1>')

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
    
    template = loader.get_template(r'mostrar_fecha.html')
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
    
    template = loader.get_template(r'prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

#===================================================================
def crear_animal(request):
    animal = Animal(nombre= 'Toncha 2', edad= 3)
    print(animal.nombre)
    print(animal.edad)
    animal.save()
    datos={'animal': animal}
    template = loader.get_template(r'crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)