# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class MasterFiltroSIE(models.Model):
     identidicador=models.IntegerField()
     descripcion = models.CharField(max_length=100)  # Field name made lowercase.
     tabla = models.CharField(max_length=100,blank=True)  # Field name made lowercase.
     nombre = models.CharField(max_length=100)  # Field name made lowercase.
     alias = models.CharField(max_length=100)  # Field name made lowercase.
     tipocampo = models.CharField(max_length=100)  # Field name made lowercase

     def __str__(self):
      return self.nombre


