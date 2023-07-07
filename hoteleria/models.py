from django.db import models

# Create your models here.


class Habitacionm(models.Model):
    id = models.AutoField(primary_key=True)
    nhabitacion = models.IntegerField(verbose_name='Numero de habitación')
    cantidadpas = models.IntegerField(verbose_name='Cantidad pasajeros admitidos')
    orientacionhab = models.CharField(max_length=100, verbose_name='Orientación habitación')
    estadohab = models.CharField(max_length=100, verbose_name= 'Estado habitación')


    def __str__(self):
        fila = 'Habitacion numero ' + str(self.nhabitacion)
        return fila


class Pasajerom(models.Model):
    id = models.AutoField(primary_key=True)
    rpasajero = models.CharField(max_length=50,verbose_name='Rut pasajero')
    nombrepasajero = models.CharField(max_length=50, verbose_name='Nombre completo pasajero')
    pasajeroresponsable = models.CharField(max_length=2,verbose_name='Pasajero responsable Si o No')
    nhabitacionpas = models.IntegerField(verbose_name='Número de habitación de pasajero')
    cargo = models.IntegerField(verbose_name= 'Cargo de habitación por pasajero')


    def __str__(self):
        fila = 'Pasajero ' + str(self.nombrepasajero)
        return fila


