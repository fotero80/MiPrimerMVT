from django.urls import path
from MiPrimerMVTApp.views import cargar_libros, cargar_autores, cargar_editoriales, cargar_clasificaciones, Main

urlpatterns = [
    path('',Main, name='MiPrimerMVTAppMain'),
    path('CargaLibros/<nombre>/<cantidadHojas>', cargar_libros, name='MiPrimerMVTAppCargarLibros'),
    path('CargaAutores/<nombre>/<apellido>', cargar_autores, name='MiPrimerMVTAppCargarAutores'),
    path('CargaEditoriales/<nombre>/<direccion>/<email>', cargar_editoriales, name='MiPrimerMVTAppCargarEditoriales'),
    path('CargaClasificaciones/<tipo>', cargar_clasificaciones, name='MiPrimerMVTAppCargarClasificaciones'),
]