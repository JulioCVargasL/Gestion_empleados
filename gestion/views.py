from django.shortcuts import render
from django.http import HttpResponse
from .models import empleados,puesto_trabajo,fabricas,salarios,poblacion,pais
# Create your views here.
def index(request):

  return render(request, 'index.html', {})

def salario(request):

def puesto(request):
  salario = Salario
