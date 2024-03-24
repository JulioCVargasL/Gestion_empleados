from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleados,Puesto_trabajo,Fabricas,Salarios,Poblacion,Pais
# Create your views here.
def index(request):

  return render(request, 'index.html', {})

def salario(request):
  return render(request, 'salario.html', {})

def saveSalario(request):
  
  if 'extra_dec' in request.POST:
    extra_dec = True
  else:
    extra_dec = False
  if 'extra_jun' in request.POST:
    extra_jun = True
  else:
    extra_jun = False

  valor_bruto = request.POST['valor_bruto']

  salario     = Salarios(valor_bruto=valor_bruto, extra_dec=extra_dec, extra_jun=extra_jun)
  salario.save()
 
  return HttpResponse("Salario Creado")

def puesto(request):
 salario = Salarios.objects.all()
 return render(request, 'puesto.html', {'salario': Salarios})

def savePuesto(request):
  nombrePuesto  = request.POST['nombre_pu']
  descripcion   = request.POST['descripcion']
  valor_bruto   = Salarios.objects.get(id=request.POST['salario'])
  puesto        = Puesto_trabajo(nombrePuesto=nombrePuesto, descripcion=descripcion, valor_bruto=valor_bruto)
  puesto.save()
  return HttpResponse("Puesto de trabajo creado")