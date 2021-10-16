from rest_framework          import serializers
from mediApp.models.paciente import Paciente
from mediApp.models.user     import User
from mediApp.models.entidad  import Entidad

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'user', 'entidad']

    def to_representation(self, obj):
        user = User.objects.get(id=obj.user.id)
        entidad = Entidad.objects.get(id=obj.entidad.id)
        paciente = Paciente.objects.get(id=obj.id)

        return{
            'id': paciente.id,
            'user': {
                'username': user.username,
                'cedula': user.cedula,
                'nombres': user.nombres,
                'apellidos': user.apellidos,
                'telefono': user.telefono,
                'email': user.email,
            },
            'entidad': entidad.tipo,
        }