from django.contrib import admin
from indicadores.models import *
# Register your models here.
class IndicadorAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Descripcion_Concepto','Descripcion_Operacion','Otro')

admin.site.register(Indicador, IndicadorAdmin)


