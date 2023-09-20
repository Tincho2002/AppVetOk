from django.db import models

# Create your models here.

class Alimentos(models.Model):
    marca = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    mascota = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.marca} - {self.tipo} - {self.mascota}"

class Accesorios(models.Model):
    marca = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    mascota = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.marca} - {self.tipo} - {self.mascota}"

class Juguetes(models.Model):
    marca = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    mascota = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.marca} - {self.tipo} - {self.mascota}"
