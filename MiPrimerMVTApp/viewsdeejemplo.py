from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from MiPrimerMVTApp.models import CargarLibros


def libros(request, nombre, cantidadHojas):
    with open("Template/templateLibros.html", "r") as f:
        plantilla = Template(f.read())
        variables = {
            "NombreLibro": nombre,
            "CantidadHojas": cantidadHojas
        }
    contexto = Context(variables)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def cargar_libros(request, nombre, cantidadHojas):
    lib = CargarLibros(nombre=nombre, cantidadHojas=cantidadHojas)
    lib.save()
    plantilla = loader.get_template('templateLibros.html')
    contexto = {
        "NombreLibro": lib.nombre,
        "CantidadHojas": lib.cantidadHojas
    }
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def mi_nombre(request, nombre):
    text_response = f"El nombre ingresado es {nombre}"
    return HttpResponse(text_response)


def probando_template(request, nombre):
    with open("Template/template1.html", "r") as f:
        plantilla = Template(f.read())
        variables = {
            "dato1": "hola mundo",
            "dato2": "Fernando",
            "dato3": datetime.now(),
            "dato4": nombre,
            "lista": [1, 2, 3, 4]
        }
    contexto = Context(variables)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
