from django.db import models
from .paciente import Paciente

from datetime import date

class Pregunta(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='paciente_pregunta', on_delete=models.CASCADE)
    pregunta = models.CharField('Pregunta', max_length=350)
    fecha = models.DateField('Fecha', auto_now=True)