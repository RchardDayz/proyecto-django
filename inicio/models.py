from django.db import models

# Create your models here.
'''CharField va a escribir en columnas'''
class Animal(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    
    def __str__(self):
        return  f'Mi nombre es: {self.nombre}, Mi edad es: {self.edad}'
    
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return  f' Nombre: {self.nombre} {self.apellido}'
    
    
