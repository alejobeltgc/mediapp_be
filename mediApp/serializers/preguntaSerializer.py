from rest_framework import serializers
from mediApp.models.pregunta import Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id', 'paciente', 'titulo', 'pregunta', 'fecha']
    