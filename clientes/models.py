# clientes/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.cliente} el {self.fecha} a las {self.hora}"

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    observaciones = models.TextField()

    def __str__(self):
        return f"Historial de {self.cliente} - {self.tratamiento}"
