from django.db import models

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    especialidad = models.CharField('Especialidad', max_length=30)