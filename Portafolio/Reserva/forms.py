from django.contrib.auth.models import User
from django import forms
from .models import Contacto, Registro, RegistroReparacion
from django.contrib.auth.forms import UserCreationForm


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ["run", "nombre", "apellido", "email", "telefono", "dia",
                  "fecha_nacimiento", "comuna", "lateralidad"]
        # fields = '__all__' -- esto es en caoso que quiera ocupar tod los campos del modelo



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username',"first_name","last_name","email","password1","password2"]



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields =  '__all__'


class ReparacionForm(forms.ModelForm):
    class Meta:
        model = RegistroReparacion
        fields =  '__all__'
