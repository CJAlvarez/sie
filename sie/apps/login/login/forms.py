# __author__ = 'alejandro'
#  !/usr/bin/env python
#  -*- encoding: utf-8 -*-
from django import forms
#
# from siemodels import *
from  sie.apps.login.models import *
#
#
class ProcesoForm(forms.ModelForm):
    class Meta:
         model = ProcesoEducativo
         exclude=['']
#         fields=['numero_identidad']

#
class ParticipantesForm(forms.ModelForm):
    class Meta:
         model = Personas
         exclude=['']
         #fields=['']

class ProyectosForm(forms.ModelForm):
    class Meta:
         model = Proyectos
         exclude=['']
#        # fields=['']


#         #fields=['clave','cd_id','cecap_id','clavececap']
#
#
class StaffFacilitadoresForm(forms.ModelForm):
    class Meta:
         model = Cateducadores
         exclude=['']



#
#
class PersonasporprocesoForm(forms.ModelForm):
    causappaldesercion = forms.CharField(widget=forms.Textarea(attrs={'size': '40'}))
    class Meta:
         model = Personasporprocesoeducativo
         exclude=['']
#        # fields=['']
#
#



class modulosForm(forms.ModelForm):
    class Meta:
         model = Modulos
         exclude=['']
#        # fields=['']
#