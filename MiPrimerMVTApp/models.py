from django.db import models


class Libros(models.Model):
    nombre = models.CharField(max_length=50)
    cantidadHojas = models.IntegerField()


class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


class Editoriales(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()


class Clasificaciones(models.Model):
    tipo = models.CharField(max_length=50)
