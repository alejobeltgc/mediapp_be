from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from mediApp.models.medico import Medico
from mediApp.serializers.medicoSerializer import MedicoSerializer

class MedicoView(generics.ListAPIView):
    serializer_class = MedicoSerializer
    permission_class = (IsAuthenticated,)
    queryset = Medico.objects.all()

    print(queryset)

    def get(self, request, *args, **kwargs):
        print("Req: ", self.request)
        print("Arg: ", self.args)
        print("KWA: ", self.kwargs)

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)
