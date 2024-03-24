from django.urls import path
from . import views

urlpatterns = [
    path('',              views.index,        name="inicio"),
    path('salario/',       views.salario,      name="salario"),
    path('saveSalario/',  views.saveSalario,  name="saveSalario"),
    path('puesto/',       views.puesto,       name="puesto"),
    # path('savePuesto/',   views.savePuesto,   name="savePuesto"),

]

