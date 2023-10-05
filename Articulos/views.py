from django.shortcuts import render
from Articulos.models import Entrada,Comentario
from Articulos.forms import ComentarioForm
from django.http import HttpResponse
# Create your views here.
def home (request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
           nombre = form.cleaned_data['nombre']
           comentario = form.cleaned_data['comentario']
           obj = Comentario(nombre=nombre,Comentario=comentario)
           obj.save()
           mensaje = "Tu mensaje fue recibido correctamente"
           return render(request,"bienvenida.html",{"articulos":articulos,"mensaje":mensaje,"form":form})
    form = ComentarioForm()
    return render (request, "bienvenida.html",{"articulos":articulos,"form":form})
def Cursorobotica(request):
    return render(request, "Cursorobotica.html")

def busqueda (request):
    return render(request, "busqueda.html")

def buscar(request):
    respuesta = f"Estoy buscando: {request.GET.get('comentario', '')}"
    comentario = request.GET.get('comentario', '')

    if comentario:
        cursos = Comentario.objects.filter(comentario__icontains=Comentario)
        return render(request, "resultadosbusqueda.html", {"cursos": cursos, "comentario": comentario})
    else:
        respuesta = "No tuviste respuesta"
        return HttpResponse(respuesta)
