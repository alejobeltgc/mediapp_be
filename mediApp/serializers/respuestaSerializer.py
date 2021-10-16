from rest_framework import serializers
from rest_framework.response import Response
from mediApp.models.respuesta import Respuesta

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['id', 'medico', 'pregunta', 'respuesta']
