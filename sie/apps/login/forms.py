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
    cecap_id = forms.IntegerField(widget=forms.TextInput(attrs={'size': '40','readonly':'readonly'}))
    clavececap = forms.CharField(widget=forms.TextInput(attrs={'size': '40','readonly':'readonly'}))
    clave = forms.CharField(widget=forms.TextInput(attrs={'size': '40','readonly':'readonly'}))
    cd_id = forms.CharField(widget=forms.TextInput(attrs={'size': '40','readonly':'readonly'}))
   # Donde_desarrollara_proceso = forms.ChoiceField(choices=CHOICES)
    #Donde_desarrollara_proceso = forms.ChoiceField(choices=a)
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
 #   claveev = forms.CharField(widget=forms.Select(attrs={'size': '40'}))
    CHOICES = (('0','Ninguna'),
                ('1','Cambio de Domicilio'),
                ('2','Migro a la Ciudad'),
               ('3', 'Migro a otro pais'),
               ('4', 'Muerte Familiar Cercano'),
               ('5', 'Desmotivacion'),
               ('6', 'Otras'),

               )
    causappaldesercion = forms.ChoiceField(choices=CHOICES)


    class Meta:
         model = Personasporprocesoeducativo
         exclude=['pxp_id','per_id','ev_id','obscecap','edad','tipocertificado']
#        # fields=['']
#+
#




class modulosForm(forms.ModelForm):
    class Meta:
         model = Modulos
         exclude=['']
#        # fields=['']
#


class UserForm(forms.ModelForm):

    class Meta:
        model = Perfil
        exclude=['']
        fields=['id','username','password','first_name','last_name','email']

    def save(self,commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data["email"]
        user.is_active = True
        if commit:
            user.save()
        return user
