from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns( 'indicadores.views',
	url(r'^search/$', 'search', name ='vista_buscar_indicadores'),
	url(r'^insertar/$', 'addIndicador', name='insertar'),
	url(r'^nuevo_tipo/$', 'addTipo_Indicador', name='nuevo_tipo'),
	url(r'^$', MostrarEstadisticas.as_view(), name='estadisticas'),
	url(r'^ajax/$', ajax_Estadisticas.as_view(), name='ajax_estadisticas'),
	url(r'^tipo/(?P<tipo_indicador>.*)/$', 'tipo_indicador_view', name='tipo_indicador'),    
    url(r'^paget/(?P<pagina>.*)/$', 'tipo_indicadores_view', name='tipo_indicadores'),
    url(r'^editar/(?P<id_ind>.*)/$', 'editar_indicador_view', name = 'editar_indicador'),
    url(r'^editar_tipo/(?P<id_ind>.*)/$', 'editar_tipo_indicador_view', name = 'editar_tipo_indicador'),
    url(r'^(?P<indicador>.*)/$', 'indicador_view', name='indicador'), 
     

)
