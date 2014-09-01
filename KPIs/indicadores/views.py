from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import KPIs.settings
import django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from indicadores.forms import *
import simplejson
from indicadores.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(Nombre__icontains=query))
		results = Tipo_indicador.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("indicador/search.html", {'results': results,	'query': query})

@login_required()
def addIndicador(request):
	info = "Inicializando" 
	if request.method == "POST":
		form = addIndicadorForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False) 
			add.status = True
			add.save() #Guarda la informacion
			form.save_m2m() # guarda las relaciones de ManyToMany
			info = "Se guardo satisfactoriamente!!!!!"
			return HttpResponseRedirect('/indicador/insertar/')
	else:
		form = addIndicadorForm()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('indicador/insertar.html',ctx,context_instance=RequestContext(request))

@login_required()
def addTipo_Indicador(request):
	info = "Inicializando" 
	if request.method == "POST":
		form = addTipo(request.POST)
		if form.is_valid():
			add = form.save(commit=False) 
			add.status = True
			add.save() #Guarda la informacion			
			info = "Se guardo satisfactoriamente!!!!!"
			return HttpResponseRedirect('/indicador/nuevo_tipo/')
	else:
		form = addTipo()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('indicador/nuevo_tipo.html',ctx,context_instance=RequestContext(request))

def tipo_indicadores_view(request,pagina):
	if request.method=="POST":
		if "tipo_indicador_id" in request.POST:
			try:
				id_indicador = request.POST['tipo_indicador_id']
				p = Tipo_indicador.objects.get(pk=id_indicador)
				mensaje = {"status":"True","tipo_indicador_id":p.id}
				p.delete() 
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_indicador = Tipo_indicador.objects.all() 
	paginator = Paginator(lista_indicador,6)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		indicadores = paginator.page(page)
	except (EmptyPage,InvalidPage):
		indicadores = paginator.page(paginator.num_pages)
	ctx = {'indicadores':indicadores, 'lista':lista_indicador}
	return render_to_response('indicador/tipo_indicadores.html',ctx,context_instance=RequestContext(request))



def tipo_indicador_view (request, tipo_indicador):
	i = tipo_indicador
	indicador = Tipo_indicador.objects.get(pk=i)
	return render (request, 'indicador/single_tipo.html', {'indicador':indicador})

def indicador_view (request, indicador):
	i = indicador
	indicador = Indicador.objects.get(pk=i)
	return render (request, 'indicador/single.html', {'indicador':indicador})


def login_view(request):
	mensaje= ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				next = request.POST['next']

				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username = username, password = password)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect(next)
				else:
					mensaje = "usuario y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginForm()
		ctx = {'form':form,'mensage':mensaje, 'next':next}
		return render_to_response('login.html', ctx, context_instance=RequestContext(request))
							
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def registro_view(request):
	form = RegistroForm()
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario, email=email, password=password_one)
			u.save()# Guardar el objeto
			return render_to_response('Gracias_Registro.html', context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('registro.html', ctx, context_instance=RequestContext(request))
	ctx = {'form':form}

	return render_to_response('registro.html',ctx,  context_instance=RequestContext(request))

def editar_indicador_view(request, id_ind):
	ind = Indicador.objects.get(id=id_ind)
	if request.method == "POST":
		form = addIndicadorForm(request.POST,request.FILES, instance=ind) # recibimos tambien una instancia
		if form.is_valid():
			edit_ind =  form.save(commit=False)
			edit_ind.status = id_ind
			edit_ind.save()
			return HttpResponseRedirect('/indicador/%s'%edit_ind.id)
		
	else: 
		form = addIndicadorForm(instance=ind)
	ctx = {'form':form,'indicador':ind}
	return render_to_response('indicador/editar.html',ctx,context_instance=RequestContext(request))

	
def editar_tipo_indicador_view(request, id_ind):
	ind = Tipo_indicador.objects.get(id=id_ind)
	if request.method == "POST":
		form = addTipo(request.POST,request.FILES, instance=ind) # recibimos tambien una instancia
		if form.is_valid():
			edit_ind =  form.save(commit=False)
			edit_ind.status = id_ind
			edit_ind.save()
			return HttpResponseRedirect('/indicador/tipo/%s'%edit_ind.id)
		
	else: 
		form = addTipo(instance=ind)
	ctx = {'form':form,'indicador':ind}
	return render_to_response('indicador/editar_tipo.html',ctx,context_instance=RequestContext(request))


class MostrarEstadisticas(ListView):
	model = Tipo_indicador
	template_name = 'indicador/estadisticas.html'
	context_object_name='tipos'

from django.core import serializers

class ajax_Estadisticas(TemplateView):

	def get(self, request, *args, **kwargs):
		id_tipo= request.GET['id']
		kpis = Indicador.objects.filter(tipo__id=id_tipo).order_by('fecha')
		data = serializers.serialize('json', kpis, fields=('fecha', 'valor_estimado','valor_real'))
		return HttpResponse(data, mimetype='application/json')
