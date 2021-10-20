from django.db import models


# Create your models here.
from django.forms import EmailField


class Plant(models.Model):
    name = models.CharField(verbose_name='Nombre de la planta', max_length=80)
    description = models.TextField(verbose_name='Descripción', max_length=600)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'


ESPECIALIDADES = [('esp1', 'Pediatría'), ('esp2', 'Ortodoncia'), ('esp3', 'Partos'), ('esp4', 'Cirujano'), ('esp5', 'Quiropráctico')]


class Medico(models.Model):
    nombre = models.CharField(verbose_name='Nombre del médico', max_length=50)
    apellidoPaterno = models.CharField(verbose_name='Apellido Paterno', max_length=50)
    apellidoMaterno = models.CharField(verbose_name='Apellido Materno', max_length=50)
    fechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    especialidad = models.CharField(choices=ESPECIALIDADES, verbose_name='Elige especialidad', max_length=15)
    telefono = models.CharField(verbose_name='Ingrese teléfono', max_length=15)
    email = models.EmailField(verbose_name='Correo electrónico', max_length=100)

    def __str__(self):
        return self.nombre + ' ' + self.apellidoPaterno + " " + self.apellidoMaterno

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Persona(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


