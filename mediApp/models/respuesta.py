from django.db import models
from .medico import Medico
from .pregunta import Pregunta

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, related_name='medico_respuesta', on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, related_name='pregunta_respuesta', on_delete=models.CASCADE)
    respuesta = models.CharField('Respuesta', max_length=350)