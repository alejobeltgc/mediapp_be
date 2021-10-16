from rest_framework import serializers
from mediApp.models.especialidad import Especialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'especialidad']

    def to_representation(self, obj):
        especialidad = Especialidad.objects.get(id=obj.id)

        return {
            'id': especialidad.id,
            'especialidad': especialidad.especialidad
        }