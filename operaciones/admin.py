from django.contrib import admin
from .models import (
    Kit, Llave, Ruta, Proceso, Estacion, 
    MovimientosEstacion, Coordinador, Operador,
    ReporteDiario, RegistroDespliegue)

# Register your models here.

admin.site.register(Kit)
admin.site.register(Llave)
admin.site.register(Ruta)
admin.site.register(Proceso)
admin.site.register(Estacion)
admin.site.register(MovimientosEstacion)
admin.site.register(Coordinador)
admin.site.register(Operador)
admin.site.register(ReporteDiario)
admin.site.register(RegistroDespliegue)