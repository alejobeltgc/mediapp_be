from rest_framework import serializers
from mediApp.models.entidad import Entidad

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = ['id', 'tipo']
    
    def to_representation(self, obj):
        entidad = Entidad.objects.get(id=obj.id)

        return {
            'id': entidad.id,
            'tipo': entidad.tipo
        }