from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):	
	return render (request, 'index.html')

@login_required()
def about(request):
	texto = "Proyecto de Indicadores (KPIs) -  Sergio Alexander Gutierrez - CodeTag"
	return render (request, 'about.html', {'texto': texto})



