from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KPIs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/', 'KPIs.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^indicador/', include ('indicadores.urls')),
    url(r'^$', 'KPIs.views.inicio', name='index'),
    url(r'^login/$', 'indicadores.views.login_view', name = 'vista_login'),
	url(r'^logout/$', 'indicadores.views.logout_view', name = 'vista_logout'),
	url(r'^registro/$', 'indicadores.views.registro_view', name = 'vista_registro'),
)