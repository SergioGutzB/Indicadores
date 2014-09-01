from django.contrib import admin
from indicadores.models import *
# Register your models here.
class IndicadorAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'valor_estimado', 'valor_real')

class Tipo_indicadorAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Descripcion_Concepto')

admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(Tipo_indicador, Tipo_indicadorAdmin)