from django.urls import path
from MiPrimerMVTApp.views import cargar_libros, cargar_autores, cargar_editoriales, cargar_clasificaciones, Main

urlpatterns = [
    path('',Main),
    path('CargaLibros/<nombre>/<cantidadHojas>', cargar_libros),
    path('CargaAutores/<nombre>/<apellido>', cargar_autores),
    path('CargaEditoriales/<nombre>/<direccion>/<email>', cargar_editoriales),
    path('CargaClasificaciones/<tipo>', cargar_clasificaciones),
]