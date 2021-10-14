from django.db     import models
from .user         import User
from .especialidad import Especialidad

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='medico', on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, related_name='especialidad_medico', on_delete=models.CASCADE)
    experiencia = models.IntegerField('Experiencia')