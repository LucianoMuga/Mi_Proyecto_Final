from django.contrib import admin
from django.urls import path
from ejemplo.views import index, indexDos, indexTres, mostrarFamilia, mostrarFamiliar, BuscarFamiliar
from blog.views import index as blog_index

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("saludar/", index),
    path("saludar2/", indexDos),
    path("mostrar_notas/", indexTres),
    path("mostrar_familia/", mostrarFamilia), 
    path("mostrar-familiares/", mostrarFamiliar), # Este es el entregable.
    path("blog/", blog_index),
    path("mi-familia/buscar", BuscarFamiliar.as_view())
]
