from django.http import HttpResponse    
from datetime import datetime
from django.template import Template, context

def mi_vista(request):
    return HttpResponse('<h1>Mi primera Vista</h1>')

def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    return HttpResponse(f'<p>{dt_formateado}</p>')

def saludar(request):
    return HttpResponse('<h1>Hola Ricardo Diaz</h1>')

def mi_primer_plantilla(request):
    
    archivo = open(r'C:\Users\Rdiaz\OneDrive\RICARDO DIAZ\CURSO PYTHON\CODERHOUSE\CLASES\DJANGO\proyecto-django\templates\mi_primer_plantilla.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)
