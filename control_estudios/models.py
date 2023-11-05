from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField()
    profesion = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=64)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        if self.entregado == True:
            return f"{self.nombre} (Entregado)"
        else:
            return f"{self.nombre} (No entregado)"

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.comision})"