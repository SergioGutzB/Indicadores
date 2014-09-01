from django.db import models

# Create your models here.
class Tipo_indicador(models.Model):
	Nombre = models.CharField(max_length=200)
	Descripcion_Concepto = models.TextField()

	def __unicode__ (self):
		return self.Nombre

class Indicador(models.Model):
	tipo = models.ForeignKey(Tipo_indicador)
	fecha = models.DateField()
	valor_estimado = models.DecimalField(max_digits=8, decimal_places=2)
	valor_real = models.DecimalField(max_digits=8, decimal_places=2)
