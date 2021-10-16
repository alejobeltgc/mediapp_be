from rest_framework                             import serializers
from mediApp.models.user                        import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cedula', 'nombres', 'apellidos', 'telefono', 'email', 'password']

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
            
        return {
            'id': user.id,
            'username': user.username,
            'cedula': user.cedula,
            'nombres': user.nombres,
            'apellidos': user.apellidos,
            'telefono': user.telefono,
            'email': user.email,
        }