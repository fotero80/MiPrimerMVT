from datetime import datetime
from django.shortcuts import render
from MiPrimerMVTApp.models import Libros, Autores, Editoriales, Clasificaciones

def cargar_libros(request, nombre, cantidadHojas):
    lib = Libros(nombre=nombre, cantidadHojas=cantidadHojas)
    lib.save()
    contexto = {
        "NombreLibro": lib.nombre,
        "CantidadHojas": lib.cantidadHojas,
        "Fecha": datetime.now()
    }
    return render(request, 'templateLibros.html', contexto)

def cargar_autores(request, nombre, apellido):
    aut = Autores(nombre=nombre, apellido=apellido)
    aut.save()
    contexto = {
        "NombreAutor": aut.nombre,
        "ApellidoAutor": aut.apellido,
        "Fecha": datetime.now()
    }
    return render(request, 'templateAutores.html', contexto)

def cargar_editoriales(request, nombre, direccion, email):
    edi = Editoriales(nombre=nombre, direccion=direccion, email=email)
    edi.save()
    contexto = {
        "NombreEditorial": edi.nombre,
        "DireccionEditorial": edi.direccion,
        "EmailEditorial": edi.email,
        "Fecha": datetime.now()
    }
    return render(request, 'templateEditoriales.html', contexto)

def cargar_clasificaciones(request, tipo):
    cla = Clasificaciones(tipo=tipo)
    cla.save()
    contexto = {
        "TipoClasificaciones": cla.tipo,
        "Fecha": datetime.now()
    }
    return render(request, 'templateClasificaciones.html', contexto)