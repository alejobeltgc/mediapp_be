from django.db import models

class Entidad(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField('Tipo_Entidad', max_length=30)