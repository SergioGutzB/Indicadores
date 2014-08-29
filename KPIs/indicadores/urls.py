from django.conf.urls import patterns, include, url

urlpatterns = patterns( 'indicadores.views',
	url(r'^search/$', 'search', name ='vista_buscar_indicadores'),
	url(r'^insertar/$', 'addIndicador', name='insertar'),
    url(r'^page/(?P<pagina>.*)/$', 'indicadores_view', name='indicadores'),
    url(r'^editar/(?P<id_ind>.*)/$', 'editar_indicador_view', name = 'editar_indicador'),
    url(r'^(?P<indicador>.*)/$', 'indicador_view', name='indicador'),    
)
