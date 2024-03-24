from django.db import models

# Create your models here.

class Salarios(models.Model):
  valor_bruto = models.IntegerField()
  extra_dec = models.BooleanField(default=False)
  extra_jun = models.BooleanField(default=False)

class Puesto_trabajo(models.Model):
  nombre_pu = models.CharField(max_length=30)
  descripcion = models.TextField()
  salarios = models.ForeignKey(Salarios, on_delete=models.CASCADE)

class Pais(models.Model):
  nombre_pais = models.CharField(max_length=40)

class Poblacion(models.Model):
  nombre_pob = models.CharField(max_length=40)
  pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Fabricas(models.Model):
  nombre_fab = models.CharField(max_length=30)
  direccion = models.CharField(max_length=30)
  codigo_postal = models.IntegerField()
  poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)

class Empleados(models.Model):
  nombre_em = models.CharField(max_length=30)
  documento = models.IntegerField()
  email = models.EmailField()
  direccion_em = models.CharField(max_length=30)
  puesto = models.ForeignKey(Puesto_trabajo, on_delete=models.CASCADE)
  fabrica = models.ForeignKey(Fabricas, on_delete=models.CASCADE)