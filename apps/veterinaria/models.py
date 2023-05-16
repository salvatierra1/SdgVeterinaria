from datetime import datetime
from django import forms
from django.db import models

# Create your models here.

#Clase Cliente
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.PositiveIntegerField(verbose_name="D.N.I", unique=True, blank=True)
    nombre= models.CharField(verbose_name="Nombre/s", max_length=30)
    apellido=models.CharField(verbose_name="Apellido/s", max_length=30)
    ciudad=models.CharField(verbose_name="Ciudad", max_length=30)
    direccion=models.CharField(verbose_name="Direccion", max_length=30)
    telefono = models.PositiveIntegerField(verbose_name='Telefono', null= True, max_length=15, blank=True)
    fecha_alta=models.DateField(verbose_name="Fecha de alta", max_length=15, default=datetime.now(), blank=True)
    estado=models.BooleanField(verbose_name="Estado", default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "cliente"
        ordering = ["id"]
     
#Clase Mascota
class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name= "propietario" )
    numero_chip = models.IntegerField(verbose_name="Numero de chip", unique=True, blank=True)
    nombre_mascota = models.CharField(verbose_name="Nombre de mascota", max_length=30)
    tipo_mascota = models.CharField(verbose_name="Tipo de mascota", max_length=30)
    estado=models.BooleanField(verbose_name="Estado", default=True)

    def __str__(self):
        return f"{self.tipo_mascota}"
    
    class Meta:
        db_table = "mascota"
        ordering = ["id"]

#Clase Historia Clinica
class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.PROTECT, verbose_name= "mascota" )
    fecha_consulta=models.DateField(verbose_name="Fecha de consulta", max_length=15, default=datetime.now(), blank=True)
    observaciones = models.TextField(verbose_name= "Observaciones", max_length=500)
    estado=models.BooleanField(verbose_name="Estado", default=True)

    def __str__(self):
        return f"{self.fecha_consulta}"
    
    class Meta:
        db_table = "historia_clinica"
        ordering = ["id"]
