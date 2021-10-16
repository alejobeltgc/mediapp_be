from rest_framework                     import serializers
from mediApp.models.medico              import Medico
from mediApp.models.user                import User
from mediApp.models.especialidad        import Especialidad

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'user', 'especialidad', 'experiencia']

    def to_representation(self, obj):
        user = User.objects.get(id=obj.user.id)
        especialidad = Especialidad.objects.get(id=obj.especialidad.id)
        medico = Medico.objects.get(id=obj.id)

        return{
            'id': medico.id,
            'experiencia': medico.experiencia,
            'user': {
                'username': user.username,
                'cedula': user.cedula,
                'nombres': user.nombres,
                'apellidos': user.apellidos,
                'telefono': user.telefono,
                'email': user.email,
            },
            'especialidad': especialidad.especialidad,
        }
