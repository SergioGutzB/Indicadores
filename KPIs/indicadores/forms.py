from django import forms
from django.contrib.auth.models import User
from indicadores.models import *


class IndicadorForm(forms.Form):
	Nombre	= forms.CharField(widget=forms.TextInput())
	Descripcion_Concepto	= forms.CharField(widget=forms.Textarea())
	Descripcion_Operacion	= forms.CharField(widget=forms.Textarea())
	Otro = forms.CharField(widget=forms.Textarea())

class addIndicadorForm(forms.ModelForm):
	class Meta:
		model = Indicador
		exclude = {'status', }

class LoginForm (forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username'}))
	password  = forms.CharField(widget=forms.PasswordInput(render_value=False))


class RegistroForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput()) 
	email  =  forms.EmailField(label="Correo Electronico", widget=forms.TextInput())
	password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username= username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya existe') 

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email= email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado') 

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email= email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado') 

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')