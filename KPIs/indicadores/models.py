from django.db import models

# Create your models here.
class Indicador(models.Model):
	Nombre = models.CharField(max_length=200)
	Descripcion_Concepto = models.TextField()
	Descripcion_Operacion = models.TextField()
	Otro = models.TextField(blank=True, null=True)
	

	def __unicode__ (self):
		return self.Nombre
