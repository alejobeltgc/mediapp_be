from django.db import models
from .user     import User
from .entidad  import Entidad

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_medico', on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, related_name='entidad_paciente', on_delete=models.CASCADE)