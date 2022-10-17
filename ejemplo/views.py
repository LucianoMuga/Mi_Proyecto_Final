from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Luciano" , "apellido" : "animal"})

def indexDos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre": nombre,
        "apellido": apellido,    
    })
    

def indexTres(request):
    return render(request, "ejemplo/saludar.html",
                  {
                      "notas": [1,2,3,4,5,6,7,8,9,10]
                  }
                
                )


def mostrarFamilia(request):
    return render(request, "ejemplo/saludar.html",
                  {
                      "familiar1" : {"Luciano", "Muga", "27/08/1996"},
                      "familiar2": {"Silvana", "Gilardoni", "21/03/1976"},
                      "familiar3": {"Claudio", "Muga", "10/09/1976"},
                  }
                )
    
def mostrarFamiliar(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})




# Create your views here.
