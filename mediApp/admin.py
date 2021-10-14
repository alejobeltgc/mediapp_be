from django.contrib import admin

from .models.pregunta      import Pregunta
from .models.respuesta     import Respuesta
from .models.paciente      import Paciente
from .models.medico        import Medico
from .models.entidad       import Entidad
from .models.especialidad  import Especialidad
from .models.user          import User


admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Entidad)
admin.site.register(Especialidad)
admin.site.register(User)
