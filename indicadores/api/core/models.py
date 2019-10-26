from django.db import models

# Create your models here.
"""Clase/Modelo dolar con dos atributos Valor del Dolar y Fecha de registro"""
class Dolar(models.Model):
    """Atributo fecha, unico valor y llave principal del modelo"""
    fecha = models.DateTimeField(primary_key = True, unique = True)
    """Valor del dolar asociado a una fecha determinada"""
    valor = models.DecimalField(max_digits = 6, decimal_places = 3)

    def __str_(self):
        return "Dolar for{}".format(self.fecha)
