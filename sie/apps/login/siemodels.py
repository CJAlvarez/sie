# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # from __future__ import unicode_literals
# from django.db import models
#
#

## class Cataldeas(models.Model):
#     idaldea = models.IntegerField(db_column='IdAldea', primary_key=True)  # Field name made lowercase.
#     nombrealdea = models.CharField(db_column='NombreAldea', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     idmunicipio = models.ForeignKey('Catmunicipios', models.DO_NOTHING, db_column='IdMunicipio', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatAldeas'
#
# class CataldeasTombstone(models.Model):
#     idaldea = models.IntegerField(db_column='IdAldea', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatAldeas_Tombstone'
#
#
# class Catcaserios(models.Model):
#     idcaserio = models.IntegerField(db_column='IdCaserio', primary_key=True)  # Field name made lowercase.
#     nombrecaserio = models.CharField(db_column='NombreCaserio', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     idaldea = models.ForeignKey(Cataldeas, models.DO_NOTHING, db_column='IdAldea', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatCaserios'
#
#
# class CatcaseriosTombstone(models.Model):
#     idcaserio = models.IntegerField(db_column='IdCaserio', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatCaserios_Tombstone'
#
#
# class Catcausasdesercion(models.Model):
#     idcausadesercion = models.AutoField(db_column='IdCausaDesercion', primary_key=True)  # Field name made lowercase.
#     causadesercion = models.CharField(db_column='CausaDesercion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatCausasDesercion'
#
#
# class CatcausasdesercionTombstone(models.Model):
#     idcausadesercion = models.IntegerField(db_column='IdCausaDesercion', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatCausasDesercion_Tombstone'
#
#
# class Catcecaps(models.Model):
#     cecap_id = models.AutoField(db_column='Cecap_Id')  # Field name made lowercase.
#     cecap_nombre = models.CharField(db_column='Cecap_Nombre', max_length=100)  # Field name made lowercase.
#     dep = models.ForeignKey('Catdepartamentos', models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     mun = models.ForeignKey('Catmunicipios', models.DO_NOTHING, db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
#     cecap_direccion = models.TextField(db_column='Cecap_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cecap_telefono = models.CharField(db_column='Cecap_Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     cecap_contacto = models.CharField(db_column='Cecap_Contacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cecap_emailcontacto = models.CharField(db_column='Cecap_EmailContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cecap_activo = models.NullBooleanField(db_column='Cecap_Activo')  # Field name made lowercase.
#     cecap_fechafundacion = models.CharField(db_column='Cecap_FechaFundacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ue = models.ForeignKey('Catunidadesejecutoras', models.DO_NOTHING, db_column='UE_Id', blank=True, null=True)  # Field name made lowercase.
#     clavececap = models.CharField(db_column='ClaveCecap', primary_key=True, max_length=10)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     def __str__(self):
#         return self.cecap_nombre
#
#     class Meta:
#         managed = False
#         db_table = 'CatCecaps'
#
#
#
#
# class CatcecapsTombstone(models.Model):
#     clavececap = models.CharField(db_column='ClaveCecap', primary_key=True, max_length=10)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatCecaps_Tombstone'
#
#
# class Catclaseeducador(models.Model):
#     cle_id = models.AutoField(db_column='Cle_Id', primary_key=True)  # Field name made lowercase.
#     cle_claseeducador = models.CharField(db_column='Cle_ClaseEducador', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatClaseEducador'
#
#
# class CatclaseeducadorTombstone(models.Model):
#     cle_id = models.IntegerField(db_column='Cle_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatClaseEducador_Tombstone'
#
#
# class Catdepartamentos(models.Model):
#     dep_id = models.IntegerField(db_column='Dep_Id', primary_key=True)  # Field name made lowercase.
#     dep_departamento = models.CharField(db_column='Dep_Departamento', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#
#     class Meta:
#         managed = False
#         db_table = 'CatDepartamentos'
#
#
# class CatdepartamentosTombstone(models.Model):
#     dep_id = models.IntegerField(db_column='Dep_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatDepartamentos_Tombstone'
#
#
# class Cateducadores(models.Model):
#     ed_id = models.CharField(db_column='Ed_Id', primary_key=True, max_length=20)  # Field name made lowercase.
#     ed_nombreeducador = models.CharField(db_column='Ed_NombreEducador', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cle = models.ForeignKey(Catclaseeducador, models.DO_NOTHING, db_column='Cle_Id', blank=True, null=True)  # Field name made lowercase.
#     ed_identidad = models.CharField(db_column='Ed_Identidad', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ed_sexo = models.CharField(db_column='Ed_Sexo', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     mun = models.ForeignKey('Catmunicipios', models.DO_NOTHING, db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
#     aldea = models.IntegerField(db_column='Aldea', blank=True, null=True)  # Field name made lowercase.
#     caserio = models.IntegerField(db_column='Caserio', blank=True, null=True)  # Field name made lowercase.
#     ed_direccion = models.TextField(db_column='Ed_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     ed_telefono = models.CharField(db_column='Ed_Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ed_celular = models.CharField(db_column='Ed_Celular', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ed_correoelectronico = models.CharField(db_column='Ed_CorreoElectronico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     et = models.ForeignKey('Catetnias', models.DO_NOTHING, db_column='Et_Id', blank=True, null=True)  # Field name made lowercase.
#     ne = models.ForeignKey('Catniveleducativo', models.DO_NOTHING, db_column='NE_Id', blank=True, null=True)  # Field name made lowercase.
#     ed_gradoalcanzado = models.CharField(db_column='Ed_GradoAlcanzado', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ec = models.ForeignKey('Catestadocivil', models.DO_NOTHING, db_column='EC_Id', blank=True, null=True)  # Field name made lowercase.
#     nac = models.ForeignKey('Catnacionalidad', models.DO_NOTHING, db_column='Nac_Id', blank=True, null=True)  # Field name made lowercase.
#     cecap_id = models.IntegerField(db_column='Cecap_Id', blank=True, null=True)  # Field name made lowercase.
#     clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#     fechanacimiento = models.DateTimeField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEducadores'
#
#
# class CateducadoresTombstone(models.Model):
#     ed_id = models.CharField(db_column='Ed_Id', primary_key=True, max_length=20)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEducadores_Tombstone'
#
#
# class Catestadocivil(models.Model):
#     ec_id = models.AutoField(db_column='EC_Id', primary_key=True)  # Field name made lowercase.
#     ec_estadocivil = models.CharField(db_column='EC_EstadoCivil', max_length=50)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEstadoCivil'
#
#
# class CatestadocivilTombstone(models.Model):
#     ec_id = models.IntegerField(db_column='EC_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEstadoCivil_Tombstone'
#
#
# class Catetnias(models.Model):
#     et_id = models.AutoField(db_column='Et_Id', primary_key=True)  # Field name made lowercase.
#     et_nombreetnia = models.CharField(db_column='Et_NombreEtnia', max_length=50)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEtnias'
#
#
# class CatetniasTombstone(models.Model):
#     et_id = models.IntegerField(db_column='Et_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEtnias_Tombstone'
#
#
# class Catevaluadores(models.Model):
#     eva_id = models.AutoField(db_column='EVA_Id', primary_key=True)  # Field name made lowercase.
#     eva_nombreevaluador = models.CharField(db_column='EVA_NombreEvaluador', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     eva_identidad = models.CharField(db_column='EVA_Identidad', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     eva_sexo = models.CharField(db_column='EVA_Sexo', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     mun = models.ForeignKey('Catmunicipios', models.DO_NOTHING, db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
#     eva_direccion = models.TextField(db_column='EVA_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     eva_telefono = models.CharField(db_column='EVA_Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     eva_celular = models.CharField(db_column='EVA_Celular', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     eva_correoelectronico = models.CharField(db_column='EVA_CorreoElectronico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     et = models.ForeignKey(Catetnias, models.DO_NOTHING, db_column='Et_Id', blank=True, null=True)  # Field name made lowercase.
#     ne = models.ForeignKey('Catniveleducativo', models.DO_NOTHING, db_column='NE_Id', blank=True, null=True)  # Field name made lowercase.
#     eva_gradoalcanzado = models.CharField(db_column='EVA_GradoAlcanzado', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ec = models.ForeignKey(Catestadocivil, models.DO_NOTHING, db_column='EC_Id', blank=True, null=True)  # Field name made lowercase.
#     nac = models.ForeignKey('Catnacionalidad', models.DO_NOTHING, db_column='Nac_Id', blank=True, null=True)  # Field name made lowercase.
#     prueba1 = models.IntegerField(db_column='Prueba1', blank=True, null=True)  # Field name made lowercase.
#     prueba2 = models.IntegerField(db_column='Prueba2', blank=True, null=True)  # Field name made lowercase.
#     prueba3 = models.IntegerField(db_column='Prueba3', blank=True, null=True)  # Field name made lowercase.
#     prueba4 = models.IntegerField(db_column='Prueba4', blank=True, null=True)  # Field name made lowercase.
#     prueba5 = models.IntegerField(db_column='Prueba5', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEvaluadores'
#
#
# class CatevaluadoresTombstone(models.Model):
#     eva_id = models.IntegerField(db_column='EVA_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatEvaluadores_Tombstone'
#
#
# class Catmaterialdidactico(models.Model):
#     md_id = models.AutoField(db_column='MD_Id', primary_key=True)  # Field name made lowercase.
#     md_materialdidactico = models.CharField(db_column='MD_MaterialDidactico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatMaterialDidactico'
#
#
# class CatmaterialdidacticoTombstone(models.Model):
#     md_id = models.IntegerField(db_column='MD_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatMaterialDidactico_Tombstone'
#
#
# class Catmetodologia(models.Model):
#     met_id = models.IntegerField(db_column='MET_Id', primary_key=True)  # Field name made lowercase.
#     met_metodologia = models.CharField(db_column='MET_Metodologia', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatMetodologia'
#
#
# class CatmetodologiaTombstone(models.Model):
#     met_id = models.IntegerField(db_column='MET_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#
#
# class Catmodalidades(models.Model):
#     mo_id = models.AutoField(db_column='MO_Id', primary_key=True)  # Field name made lowercase.
#     mo_modalidades = models.CharField(db_column='MO_Modalidades', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatModalidades'
#
#
# class CatmodalidadesTombstone(models.Model):
#     mo_id = models.IntegerField(db_column='MO_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatModalidades_Tombstone'
#
#
# class Catmunicipios(models.Model):
#     mun_id = models.IntegerField(db_column='Mun_Id', primary_key=True)  # Field name made lowercase.
#     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     mun_municipio = models.CharField(db_column='Mun_Municipio', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatMunicipios'
#
#     def __str__(self):
#      return self.mun_municipio
#
#
# class CatmunicipiosTombstone(models.Model):
#     mun_id = models.IntegerField(db_column='Mun_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatMunicipios_Tombstone'
#
#
# class Catnacionalidad(models.Model):
#     nac_id = models.AutoField(db_column='Nac_Id', primary_key=True)  # Field name made lowercase.
#     nac_nacionalidad = models.CharField(db_column='Nac_Nacionalidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatNacionalidad'
#
#
# class CatnacionalidadTombstone(models.Model):
#     nac_id = models.IntegerField(db_column='Nac_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatNacionalidad_Tombstone'
#
#
# class Catniveleducativo(models.Model):
#     ne_id = models.AutoField(db_column='NE_Id', primary_key=True)  # Field name made lowercase.
#     ne_niveleducativo = models.CharField(db_column='NE_NivelEducativo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatNivelEducativo'
#
#
# class CatniveleducativoTombstone(models.Model):
#     ne_id = models.IntegerField(db_column='NE_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatNivelEducativo_Tombstone'
#
#
# class Catopcioneseducativas(models.Model):
#     oe_id = models.AutoField(db_column='OE_Id', primary_key=True)  # Field name made lowercase.
#     oe_opcioneducativa = models.CharField(db_column='OE_OpcionEducativa', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatOpcionesEducativas'
#
#
# class CatopcioneseducativasTombstone(models.Model):
#     oe_id = models.IntegerField(db_column='OE_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatOpcionesEducativas_Tombstone'
#
#
# class Catparametros(models.Model):
#     id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
#     clave = models.CharField(db_column='Clave', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     parametro = models.CharField(db_column='Parametro', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatParametros'
#
#
# class Catpruebascertificacion(models.Model):
#     prb_id = models.AutoField(db_column='PRB_Id', primary_key=True)  # Field name made lowercase.
#     prb_nombreprueba = models.CharField(db_column='PRB_NombrePrueba', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_descripcionprueba = models.TextField(db_column='PRB_DescripcionPrueba', blank=True, null=True)  # Field name made lowercase.
#     prb_tarea1 = models.CharField(db_column='PRB_Tarea1', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea2 = models.CharField(db_column='PRB_Tarea2', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea3 = models.CharField(db_column='PRB_Tarea3', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea4 = models.CharField(db_column='PRB_Tarea4', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea5 = models.CharField(db_column='PRB_Tarea5', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea6 = models.CharField(db_column='PRB_Tarea6', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea7 = models.CharField(db_column='PRB_Tarea7', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea8 = models.CharField(db_column='PRB_Tarea8', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea9 = models.CharField(db_column='PRB_Tarea9', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea10 = models.CharField(db_column='PRB_Tarea10', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea11 = models.CharField(db_column='PRB_Tarea11', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea12 = models.CharField(db_column='PRB_Tarea12', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea13 = models.CharField(db_column='PRB_Tarea13', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea14 = models.CharField(db_column='PRB_Tarea14', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea15 = models.CharField(db_column='PRB_Tarea15', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea16 = models.CharField(db_column='PRB_Tarea16', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea17 = models.CharField(db_column='PRB_Tarea17', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea18 = models.CharField(db_column='PRB_Tarea18', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea19 = models.CharField(db_column='PRB_Tarea19', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     prb_tarea20 = models.CharField(db_column='PRB_Tarea20', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatPruebasCertificacion'
#
#
# class CatpruebascertificacionTombstone(models.Model):
#     prb_id = models.IntegerField(db_column='PRB_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatPruebasCertificacion_Tombstone'
#
#
# class Catrangoscertificados(models.Model):
#     rangoid = models.AutoField(db_column='RangoId', primary_key=True)  # Field name made lowercase.
#     rangoinferior = models.FloatField(db_column='RangoInferior', blank=True, null=True)  # Field name made lowercase.
#     rangosuperior = models.FloatField(db_column='RangoSuperior', blank=True, null=True)  # Field name made lowercase.
#     tipocertificado = models.CharField(db_column='TipoCertificado', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatRangosCertificados'
#
#
# class CatrangoscertificadosTombstone(models.Model):
#     rangoid = models.IntegerField(db_column='RangoId', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatRangosCertificados_Tombstone'
#
#
# class Catsectoreseconomicos(models.Model):
#     se_id = models.AutoField(db_column='SE_Id', primary_key=True)  # Field name made lowercase.
#     se_sectoreconomico = models.CharField(db_column='SE_SectorEconomico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatSectoresEconomicos'
#
#
# class CatsectoreseconomicosTombstone(models.Model):
#     se_id = models.IntegerField(db_column='SE_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatSectoresEconomicos_Tombstone'
#
#
# class Catsexo(models.Model):
#     id = models.DecimalField(db_column='Id', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
#     sexo = models.CharField(db_column='Sexo', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatSexo'
#
#
# class CatsexoTombstone(models.Model):
#     id = models.DecimalField(db_column='Id', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatSexo_Tombstone'
#
#
# class Cattipocalificacion(models.Model):
#     idcalificacion = models.AutoField(db_column='IdCalificacion', primary_key=True)  # Field name made lowercase.
#     tipocalificacion = models.CharField(db_column='TipoCalificacion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTipoCalificacion'
#
#
# class CattipocalificacionTombstone(models.Model):
#     idcalificacion = models.IntegerField(db_column='IdCalificacion', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTipoCalificacion_Tombstone'
#
#
# class Cattipoinstitucion(models.Model):
#     ti_id = models.AutoField(db_column='TI_Id', primary_key=True)  # Field name made lowercase.
#     ti_tipoinstitucion = models.CharField(db_column='TI_TipoInstitucion', max_length=100)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTipoInstitucion'
#
#
# class CattipoinstitucionTombstone(models.Model):
#     ti_id = models.IntegerField(db_column='TI_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTipoInstitucion_Tombstone'
#
#
# class Cattipomodalidad(models.Model):
#     tmod_id = models.AutoField(db_column='TMod_Id', primary_key=True)  # Field name made lowercase.
#     modalidadid = models.ForeignKey(Catmodalidades, models.DO_NOTHING, db_column='ModalidadId', blank=True, null=True)  # Field name made lowercase.
#     tmodo_tipomodalidad = models.CharField(db_column='TModo_TipoModalidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTipoModalidad'
#
#
# class CattipomodalidadTombstone(models.Model):
#     tmod_id = models.IntegerField(db_column='TMod_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTipoModalidad_Tombstone'
#
#
# class Cattiposadministracion(models.Model):
#     ta_id = models.AutoField(db_column='TA_Id', primary_key=True)  # Field name made lowercase.
#     ta_tipoadministracion = models.CharField(db_column='TA_TipoAdministracion', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTiposAdministracion'
#
#
# class CattiposadministracionTombstone(models.Model):
#     ta_id = models.IntegerField(db_column='TA_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTiposAdministracion_Tombstone'
#
#
# class Cattipossedes(models.Model):
#     ts_id = models.AutoField(db_column='TS_Id', primary_key=True)  # Field name made lowercase.
#     ts_tiposede = models.CharField(db_column='TS_TipoSede', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:po
#         managed = False
#         db_table = 'CatTiposSedes'
#
#
# class CattipossedesTombstone(models.Model):
#     ts_id = models.IntegerField(db_column='TS_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatTiposSedes_Tombstone'
#
#
# class Catunidadesejecutoras(models.Model):
#     ue_id = models.AutoField(db_column='UE_Id', primary_key=True)  # Field name made lowercase.
#     ue_nombre = models.CharField(db_column='UE_Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ti = models.ForeignKey(Cattipoinstitucion, models.DO_NOTHING, db_column='TI_Id', blank=True, null=True)  # Field name made lowercase.
#     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     mun = models.ForeignKey(Catmunicipios, models.DO_NOTHING, db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
#     ue_direccion = models.TextField(db_column='UE_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     ue_telefono1 = models.CharField(db_column='UE_Telefono1', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ue_telefono2 = models.CharField(db_column='UE_Telefono2', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ue_responsabletecnico = models.CharField(db_column='UE_ResponsableTecnico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ue_cargoresponsabletecnico = models.CharField(db_column='UE_CargoResponsableTecnico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ue_emailresponsabletecnico = models.CharField(db_column='UE_EmailResponsableTecnico', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ue_sitioweb = models.CharField(db_column='UE_SitioWEB', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ue_areainfluencia = models.TextField(db_column='UE_AreaInfluencia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     ue_nombrecontacto = models.CharField(db_column='UE_NombreContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ue_cargocontacto = models.CharField(db_column='UE_CargoContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ue_emailcontacto = models.CharField(db_column='UE_EmailContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatUnidadesEjecutoras'
#
#
# class CatunidadesejecutorasTombstone(models.Model):
#     ue_id = models.IntegerField(db_column='UE_Id', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CatUnidadesEjecutoras_Tombstone'
#
#
# class Eicognoscitivo(models.Model):
#     idcognoscitivo = models.IntegerField(db_column='IdCognoscitivo', primary_key=True)  # Field name made lowercase.
#     nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EICognoscitivo'
#
#
# class EicognoscitivoTombstone(models.Model):
#     idcognoscitivo = models.IntegerField(db_column='IdCognoscitivo', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EICognoscitivo_Tombstone'
#
#
# class Eifases(models.Model):
#     idfase = models.IntegerField(db_column='IdFase', primary_key=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIFases'
#
#
# class EifasesTombstone(models.Model):
#     idfase = models.IntegerField(db_column='IdFase', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIFases_Tombstone'
#
#
# class Eihabitos(models.Model):
#     idhabitos = models.IntegerField(db_column='IdHabitos', primary_key=True)  # Field name made lowercase.
#     nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIHabitos'
#
#
# class EihabitosTombstone(models.Model):
#     idhabitos = models.IntegerField(db_column='IdHabitos', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIHabitos_Tombstone'
#
#
# class Eilenguaje(models.Model):
#     idlenguaje = models.IntegerField(db_column='IdLenguaje', primary_key=True)  # Field name made lowercase.
#     nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EILenguaje'
#
#
# class EilenguajeTombstone(models.Model):
#     idlenguaje = models.IntegerField(db_column='IdLenguaje', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EILenguaje_Tombstone'
#
#
# class Eimotorfino(models.Model):
#     idmotorfino = models.IntegerField(db_column='idMotorFino', primary_key=True)  # Field name made lowercase.
#     nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIMotorFino'
#
#
# class EimotorfinoTombstone(models.Model):
#     idmotorfino = models.IntegerField(db_column='idMotorFino', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIMotorFino_Tombstone'
#
#
# class Eimotorgrueso(models.Model):
#     idmotorgrueso = models.IntegerField(db_column='IdMotorGrueso', primary_key=True)  # Field name made lowercase.
#     nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIMotorGrueso'
#
#
# class EimotorgruesoTombstone(models.Model):
#     idmotorgrueso = models.IntegerField(db_column='IdMotorGrueso', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EIMotorGrueso_Tombstone'
#
#
# class Eisocioafectivo(models.Model):
#     idsocioafectivo = models.IntegerField(db_column='IdSocioAfectivo', primary_key=True)  # Field name made lowercase.
#     nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EISocioafectivo'
#
#
# class EisocioafectivoTombstone(models.Model):
#     idsocioafectivo = models.IntegerField(db_column='IdSocioAfectivo', primary_key=True)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EISocioafectivo_Tombstone'
#
#
# class Evaleducinicial(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', max_length=20)  # Field name made lowercase.
#     numero_identidad = models.CharField(db_column='Numero_Identidad', max_length=20)  # Field name made lowercase.
#     numeroevaluacion = models.IntegerField(db_column='NumeroEvaluacion')  # Field name made lowercase.
#     fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
#     motorgrueso = models.IntegerField(db_column='MotorGrueso', blank=True, null=True)  # Field name made lowercase.
#     motorfino = models.IntegerField(db_column='MotorFino', blank=True, null=True)  # Field name made lowercase.
#     cognoscitivo = models.IntegerField(db_column='Cognoscitivo', blank=True, null=True)  # Field name made lowercase.
#     lenguaje = models.IntegerField(db_column='Lenguaje', blank=True, null=True)  # Field name made lowercase.
#     socioafectivo = models.IntegerField(db_column='SocioAfectivo', blank=True, null=True)  # Field name made lowercase.
#     habitossaludynutricion = models.IntegerField(db_column='HabitosSaludyNutricion', blank=True, null=True)  # Field name made lowercase.
#     edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EvalEducInicial'
#         unique_together = (('claveev', 'numero_identidad', 'numeroevaluacion'),)
#
#
# class EvaleducinicialTombstone(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', max_length=20)  # Field name made lowercase.
#     numero_identidad = models.CharField(db_column='Numero_Identidad', max_length=20)  # Field name made lowercase.
#     numeroevaluacion = models.IntegerField(db_column='NumeroEvaluacion')  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EvalEducInicial_Tombstone'
#         unique_together = (('claveev', 'numero_identidad', 'numeroevaluacion'),)
#
#
# class Evaluaciones(models.Model):
#     clave = models.ForeignKey('Ofertaeducativa', models.DO_NOTHING, db_column='Clave')  # Field name made lowercase.
#     claveev = models.ForeignKey('Procesoseducativos', models.DO_NOTHING, db_column='ClaveEV')  # Field name made lowercase.
#     numero_identidad = models.CharField(db_column='Numero_identidad', max_length=15)  # Field name made lowercase.
#     per_id = models.IntegerField(db_column='PER_Id', blank=True, null=True)  # Field name made lowercase.
#     ev_id = models.IntegerField(db_column='Ev_Id', blank=True, null=True)  # Field name made lowercase.
#     cd_id = models.IntegerField(db_column='CD_Id', blank=True, null=True)  # Field name made lowercase.
#     horasteoria1 = models.FloatField(db_column='HorasTeoria1', blank=True, null=True)  # Field name made lowercase.
#     horaspractica1 = models.FloatField(db_column='HorasPractica1', blank=True, null=True)  # Field name made lowercase.
#     notateorica1 = models.FloatField(db_column='NotaTeorica1', blank=True, null=True)  # Field name made lowercase.
#     notapractica1 = models.FloatField(db_column='NotaPractica1', blank=True, null=True)  # Field name made lowercase.
#     horasteoria2 = models.FloatField(db_column='HorasTeoria2', blank=True, null=True)  # Field name made lowercase.
#     horaspractica2 = models.FloatField(db_column='HorasPractica2', blank=True, null=True)  # Field name made lowercase.
#     notateorica2 = models.FloatField(db_column='NotaTeorica2', blank=True, null=True)  # Field name made lowercase.
#     notapractica2 = models.FloatField(db_column='NotaPractica2', blank=True, null=True)  # Field name made lowercase.
#     horasteoria3 = models.FloatField(db_column='HorasTeoria3', blank=True, null=True)  # Field name made lowercase.
#     horaspractica3 = models.FloatField(db_column='HorasPractica3', blank=True, null=True)  # Field name made lowercase.
#     notateorica3 = models.FloatField(db_column='NotaTeorica3', blank=True, null=True)  # Field name made lowercase.
#     notapractica3 = models.FloatField(db_column='NotaPractica3', blank=True, null=True)  # Field name made lowercase.
#     horasteoria4 = models.FloatField(db_column='HorasTeoria4', blank=True, null=True)  # Field name made lowercase.
#     horaspractica4 = models.FloatField(db_column='HorasPractica4', blank=True, null=True)  # Field name made lowercase.
#     notateorica4 = models.FloatField(db_column='NotaTeorica4', blank=True, null=True)  # Field name made lowercase.
#     notapractica4 = models.FloatField(db_column='NotaPractica4', blank=True, null=True)  # Field name made lowercase.
#     horasteoria5 = models.FloatField(db_column='HorasTeoria5', blank=True, null=True)  # Field name made lowercase.
#     horaspractica5 = models.FloatField(db_column='HorasPractica5', blank=True, null=True)  # Field name made lowercase.
#     notateorica5 = models.FloatField(db_column='NotaTeorica5', blank=True, null=True)  # Field name made lowercase.
#     notapractica5 = models.FloatField(db_column='NotaPractica5', blank=True, null=True)  # Field name made lowercase.
#     horasteoria6 = models.FloatField(db_column='HorasTeoria6', blank=True, null=True)  # Field name made lowercase.
#     horaspractica6 = models.FloatField(db_column='HorasPractica6', blank=True, null=True)  # Field name made lowercase.
#     notateorica6 = models.FloatField(db_column='NotaTeorica6', blank=True, null=True)  # Field name made lowercase.
#     notapractica6 = models.FloatField(db_column='NotaPractica6', blank=True, null=True)  # Field name made lowercase.
#     horasteoria7 = models.FloatField(db_column='HorasTeoria7', blank=True, null=True)  # Field name made lowercase.
#     horaspractica7 = models.FloatField(db_column='HorasPractica7', blank=True, null=True)  # Field name made lowercase.
#     notateorica7 = models.FloatField(db_column='NotaTeorica7', blank=True, null=True)  # Field name made lowercase.
#     notapractica7 = models.FloatField(db_column='NotaPractica7', blank=True, null=True)  # Field name made lowercase.
#     horasteoria8 = models.FloatField(db_column='HorasTeoria8', blank=True, null=True)  # Field name made lowercase.
#     horaspractica8 = models.FloatField(db_column='HorasPractica8', blank=True, null=True)  # Field name made lowercase.
#     notateorica8 = models.FloatField(db_column='NotaTeorica8', blank=True, null=True)  # Field name made lowercase.
#     notapractica8 = models.FloatField(db_column='NotaPractica8', blank=True, null=True)  # Field name made lowercase.
#     horasteoria9 = models.FloatField(db_column='HorasTeoria9', blank=True, null=True)  # Field name made lowercase.
#     horaspractica9 = models.FloatField(db_column='HorasPractica9', blank=True, null=True)  # Field name made lowercase.
#     notateorica9 = models.FloatField(db_column='NotaTeorica9', blank=True, null=True)  # Field name made lowercase.
#     notapractica9 = models.FloatField(db_column='NotaPractica9', blank=True, null=True)  # Field name made lowercase.
#     horasteoria10 = models.FloatField(db_column='HorasTeoria10', blank=True, null=True)  # Field name made lowercase.
#     horaspractica10 = models.FloatField(db_column='HorasPractica10', blank=True, null=True)  # Field name made lowercase.
#     notateorica10 = models.FloatField(db_column='NotaTeorica10', blank=True, null=True)  # Field name made lowercase.
#     notapractica10 = models.FloatField(db_column='NotaPractica10', blank=True, null=True)  # Field name made lowercase.
#     horasteoria11 = models.FloatField(db_column='HorasTeoria11', blank=True, null=True)  # Field name made lowercase.
#     horaspractica11 = models.FloatField(db_column='HorasPractica11', blank=True, null=True)  # Field name made lowercase.
#     notateorica11 = models.FloatField(db_column='NotaTeorica11', blank=True, null=True)  # Field name made lowercase.
#     notapractica11 = models.FloatField(db_column='NotaPractica11', blank=True, null=True)  # Field name made lowercase.
#     horasteoria12 = models.FloatField(db_column='HorasTeoria12', blank=True, null=True)  # Field name made lowercase.
#     horaspractica12 = models.FloatField(db_column='HorasPractica12', blank=True, null=True)  # Field name made lowercase.
#     notateorica12 = models.FloatField(db_column='NotaTeorica12', blank=True, null=True)  # Field name made lowercase.
#     notapractica12 = models.FloatField(db_column='NotaPractica12', blank=True, null=True)  # Field name made lowercase.
#     horasteoria13 = models.FloatField(db_column='HorasTeoria13', blank=True, null=True)  # Field name made lowercase.
#     horaspractica13 = models.FloatField(db_column='HorasPractica13', blank=True, null=True)  # Field name made lowercase.
#     notateorica13 = models.FloatField(db_column='NotaTeorica13', blank=True, null=True)  # Field name made lowercase.
#     notapractica13 = models.FloatField(db_column='NotaPractica13', blank=True, null=True)  # Field name made lowercase.
#     horasteoria14 = models.FloatField(db_column='HorasTeoria14', blank=True, null=True)  # Field name made lowercase.
#     horaspractica14 = models.FloatField(db_column='HorasPractica14', blank=True, null=True)  # Field name made lowercase.
#     notateorica14 = models.FloatField(db_column='NotaTeorica14', blank=True, null=True)  # Field name made lowercase.
#     notapractica14 = models.FloatField(db_column='NotaPractica14', blank=True, null=True)  # Field name made lowercase.
#     horasteoria15 = models.FloatField(db_column='HorasTeoria15', blank=True, null=True)  # Field name made lowercase.
#     horaspractica15 = models.FloatField(db_column='HorasPractica15', blank=True, null=True)  # Field name made lowercase.
#     notateorica15 = models.FloatField(db_column='NotaTeorica15', blank=True, null=True)  # Field name made lowercase.
#     notapractica15 = models.FloatField(db_column='NotaPractica15', blank=True, null=True)  # Field name made lowercase.
#     horasteoria16 = models.FloatField(db_column='HorasTeoria16', blank=True, null=True)  # Field name made lowercase.
#     horaspractica16 = models.FloatField(db_column='HorasPractica16', blank=True, null=True)  # Field name made lowercase.
#     notateorica16 = models.FloatField(db_column='NotaTeorica16', blank=True, null=True)  # Field name made lowercase.
#     notapractica16 = models.FloatField(db_column='NotaPractica16', blank=True, null=True)  # Field name made lowercase.
#     horasteoria17 = models.FloatField(db_column='HorasTeoria17', blank=True, null=True)  # Field name made lowercase.
#     horaspractica17 = models.FloatField(db_column='HorasPractica17', blank=True, null=True)  # Field name made lowercase.
#     notateorica17 = models.FloatField(db_column='NotaTeorica17', blank=True, null=True)  # Field name made lowercase.
#     notapractica17 = models.FloatField(db_column='NotaPractica17', blank=True, null=True)  # Field name made lowercase.
#     horasteoria18 = models.FloatField(db_column='HorasTeoria18', blank=True, null=True)  # Field name made lowercase.
#     horaspractica18 = models.FloatField(db_column='HorasPractica18', blank=True, null=True)  # Field name made lowercase.
#     notateorica18 = models.FloatField(db_column='NotaTeorica18', blank=True, null=True)  # Field name made lowercase.
#     notapractica18 = models.FloatField(db_column='NotaPractica18', blank=True, null=True)  # Field name made lowercase.
#     horasteoria19 = models.FloatField(db_column='HorasTeoria19', blank=True, null=True)  # Field name made lowercase.
#     horaspractica19 = models.FloatField(db_column='HorasPractica19', blank=True, null=True)  # Field name made lowercase.
#     notateorica19 = models.FloatField(db_column='NotaTeorica19', blank=True, null=True)  # Field name made lowercase.
#     notapractica19 = models.FloatField(db_column='NotaPractica19', blank=True, null=True)  # Field name made lowercase.
#     horasteoria20 = models.FloatField(db_column='HorasTeoria20', blank=True, null=True)  # Field name made lowercase.
#     horaspractica20 = models.FloatField(db_column='HorasPractica20', blank=True, null=True)  # Field name made lowercase.
#     notateorica20 = models.FloatField(db_column='NotaTeorica20', blank=True, null=True)  # Field name made lowercase.
#     notapractica20 = models.FloatField(db_column='NotaPractica20', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     pasanopasa = models.NullBooleanField(db_column='PasaNoPasa')  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#     horasteoria21 = models.FloatField(db_column='HorasTeoria21', blank=True, null=True)  # Field name made lowercase.
#     horaspractica21 = models.FloatField(db_column='HorasPractica21', blank=True, null=True)  # Field name made lowercase.
#     notateorica21 = models.FloatField(db_column='NotaTeorica21', blank=True, null=True)  # Field name made lowercase.
#     notapractica21 = models.FloatField(db_column='NotaPractica21', blank=True, null=True)  # Field name made lowercase.
#     horasteoria22 = models.FloatField(db_column='HorasTeoria22', blank=True, null=True)  # Field name made lowercase.
#     horaspractica22 = models.FloatField(db_column='HorasPractica22', blank=True, null=True)  # Field name made lowercase.
#     notateorica22 = models.FloatField(db_column='NotaTeorica22', blank=True, null=True)  # Field name made lowercase.
#     notapractica22 = models.FloatField(db_column='NotaPractica22', blank=True, null=True)  # Field name made lowercase.
#     horasteoria23 = models.FloatField(db_column='HorasTeoria23', blank=True, null=True)  # Field name made lowercase.
#     horaspractica23 = models.FloatField(db_column='HorasPractica23', blank=True, null=True)  # Field name made lowercase.
#     notateorica23 = models.FloatField(db_column='NotaTeorica23', blank=True, null=True)  # Field name made lowercase.
#     notapractica23 = models.FloatField(db_column='NotaPractica23', blank=True, null=True)  # Field name made lowercase.
#     horasteoria24 = models.FloatField(db_column='HorasTeoria24', blank=True, null=True)  # Field name made lowercase.
#     horaspractica24 = models.FloatField(db_column='HorasPractica24', blank=True, null=True)  # Field name made lowercase.
#     notateorica24 = models.FloatField(db_column='NotaTeorica24', blank=True, null=True)  # Field name made lowercase.
#     notapractica24 = models.FloatField(db_column='NotaPractica24', blank=True, null=True)  # Field name made lowercase.
#     horasteoria25 = models.FloatField(db_column='HorasTeoria25', blank=True, null=True)  # Field name made lowercase.
#     horaspractica25 = models.FloatField(db_column='HorasPractica25', blank=True, null=True)  # Field name made lowercase.
#     notateorica25 = models.FloatField(db_column='NotaTeorica25', blank=True, null=True)  # Field name made lowercase.
#     notapractica25 = models.FloatField(db_column='NotaPractica25', blank=True, null=True)  # Field name made lowercase.
#     horasteoria26 = models.FloatField(db_column='HorasTeoria26', blank=True, null=True)  # Field name made lowercase.
#     horaspractica26 = models.FloatField(db_column='HorasPractica26', blank=True, null=True)  # Field name made lowercase.
#     notateorica26 = models.FloatField(db_column='NotaTeorica26', blank=True, null=True)  # Field name made lowercase.
#     notapractica26 = models.FloatField(db_column='NotaPractica26', blank=True, null=True)  # Field name made lowercase.
#     horasteoria27 = models.FloatField(db_column='HorasTeoria27', blank=True, null=True)  # Field name made lowercase.
#     horaspractica27 = models.FloatField(db_column='HorasPractica27', blank=True, null=True)  # Field name made lowercase.
#     notateorica27 = models.FloatField(db_column='NotaTeorica27', blank=True, null=True)  # Field name made lowercase.
#     notapractica27 = models.FloatField(db_column='NotaPractica27', blank=True, null=True)  # Field name made lowercase.
#     horasteoria28 = models.FloatField(db_column='HorasTeoria28', blank=True, null=True)  # Field name made lowercase.
#     horaspractica28 = models.FloatField(db_column='HorasPractica28', blank=True, null=True)  # Field name made lowercase.
#     notateorica28 = models.FloatField(db_column='NotaTeorica28', blank=True, null=True)  # Field name made lowercase.
#     notapractica28 = models.FloatField(db_column='NotaPractica28', blank=True, null=True)  # Field name made lowercase.
#     horasteoria29 = models.FloatField(db_column='HorasTeoria29', blank=True, null=True)  # Field name made lowercase.
#     horaspractica29 = models.FloatField(db_column='HorasPractica29', blank=True, null=True)  # Field name made lowercase.
#     notateorica29 = models.FloatField(db_column='NotaTeorica29', blank=True, null=True)  # Field name made lowercase.
#     notapractica29 = models.FloatField(db_column='NotaPractica29', blank=True, null=True)  # Field name made lowercase.
#     horasteoria30 = models.FloatField(db_column='HorasTeoria30', blank=True, null=True)  # Field name made lowercase.
#     horaspractica30 = models.FloatField(db_column='HorasPractica30', blank=True, null=True)  # Field name made lowercase.
#     notateorica30 = models.FloatField(db_column='NotaTeorica30', blank=True, null=True)  # Field name made lowercase.
#     notapractica30 = models.FloatField(db_column='NotaPractica30', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Evaluaciones'
#         unique_together = (('claveev', 'numero_identidad'),)
#
#
# class EvaluacionesTombstone(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', max_length=20)  # Field name made lowercase.
#     numero_identidad = models.CharField(db_column='Numero_identidad', max_length=15)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Evaluaciones_Tombstone'
#         unique_together = (('claveev', 'numero_identidad'),)
#
#
# class Ofertaeducativa(models.Model):
#     clave = models.CharField(db_column='Clave', primary_key=True, max_length=20)  # Field name made lowercase.
#     cd_id = models.IntegerField(db_column='CD_Id', blank=True, null=True)  # Field name made lowercase.
#     cd_nombre = models.CharField(db_column='CD_Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cd_totalhoras = models.IntegerField(db_column='CD_TotalHoras', blank=True, null=True)  # Field name made lowercase.
#     cd_descripcion = models.CharField(db_column='CD_Descripcion', max_length=600, blank=True, null=True)  # Field name made lowercase.
#     cecap_id = models.IntegerField(db_column='Cecap_Id', blank=True, null=True)  # Field name made lowercase.
#     clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     nombresalida = models.CharField(db_column='NombreSalida', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     m_dulo1 = models.CharField(db_column='M\xf3dulo1', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion1 = models.CharField(db_column='Descripcion1', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras1 = models.IntegerField(db_column='NumHoras1', blank=True, null=True)  # Field name made lowercase.
#     numhorasp1 = models.IntegerField(db_column='NumHorasP1', blank=True, null=True)  # Field name made lowercase.
#     m_dulo2 = models.CharField(db_column='M\xf3dulo2', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion2 = models.CharField(db_column='Descripcion2', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras2 = models.IntegerField(db_column='NumHoras2', blank=True, null=True)  # Field name made lowercase.
#     numhorasp2 = models.IntegerField(db_column='NumHorasP2', blank=True, null=True)  # Field name made lowercase.
#     m_dulo3 = models.CharField(db_column='M\xf3dulo3', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion3 = models.CharField(db_column='Descripcion3', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras3 = models.IntegerField(db_column='NumHoras3', blank=True, null=True)  # Field name made lowercase.
#     numhorasp3 = models.IntegerField(db_column='NumHorasP3', blank=True, null=True)  # Field name made lowercase.
#     m_dulo4 = models.CharField(db_column='M\xf3dulo4', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion4 = models.CharField(db_column='Descripcion4', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras4 = models.IntegerField(db_column='NumHoras4', blank=True, null=True)  # Field name made lowercase.
#     numhorasp4 = models.IntegerField(db_column='NumHorasP4', blank=True, null=True)  # Field name made lowercase.
#     m_dulo5 = models.CharField(db_column='M\xf3dulo5', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion5 = models.CharField(db_column='Descripcion5', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras5 = models.IntegerField(db_column='NumHoras5', blank=True, null=True)  # Field name made lowercase.
#     numhorasp5 = models.IntegerField(db_column='NumHorasP5', blank=True, null=True)  # Field name made lowercase.
#     m_dulo6 = models.CharField(db_column='M\xf3dulo6', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion6 = models.CharField(db_column='Descripcion6', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras6 = models.IntegerField(db_column='NumHoras6', blank=True, null=True)  # Field name made lowercase.
#     numhorasp6 = models.IntegerField(db_column='NumHorasP6', blank=True, null=True)  # Field name made lowercase.
#     m_dulo7 = models.CharField(db_column='M\xf3dulo7', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion7 = models.CharField(db_column='Descripcion7', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras7 = models.IntegerField(db_column='NumHoras7', blank=True, null=True)  # Field name made lowercase.
#     numhorasp7 = models.IntegerField(db_column='NumHorasP7', blank=True, null=True)  # Field name made lowercase.
#     m_dulo8 = models.CharField(db_column='M\xf3dulo8', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion8 = models.CharField(db_column='Descripcion8', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras8 = models.IntegerField(db_column='NumHoras8', blank=True, null=True)  # Field name made lowercase.
#     numhorasp8 = models.IntegerField(db_column='NumHorasP8', blank=True, null=True)  # Field name made lowercase.
#     m_dulo9 = models.CharField(db_column='M\xf3dulo9', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion9 = models.CharField(db_column='Descripcion9', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras9 = models.IntegerField(db_column='NumHoras9', blank=True, null=True)  # Field name made lowercase.
#     numhorasp9 = models.IntegerField(db_column='NumHorasP9', blank=True, null=True)  # Field name made lowercase.
#     m_dulo10 = models.CharField(db_column='M\xf3dulo10', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion10 = models.CharField(db_column='Descripcion10', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras10 = models.IntegerField(db_column='NumHoras10', blank=True, null=True)  # Field name made lowercase.
#     numhorasp10 = models.IntegerField(db_column='NumHorasP10', blank=True, null=True)  # Field name made lowercase.
#     m_dulo11 = models.CharField(db_column='M\xf3dulo11', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion11 = models.CharField(db_column='Descripcion11', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras11 = models.IntegerField(db_column='NumHoras11', blank=True, null=True)  # Field name made lowercase.
#     numhorasp11 = models.IntegerField(db_column='NumHorasP11', blank=True, null=True)  # Field name made lowercase.
#     m_dulo12 = models.CharField(db_column='M\xf3dulo12', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion12 = models.CharField(db_column='Descripcion12', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras12 = models.IntegerField(db_column='NumHoras12', blank=True, null=True)  # Field name made lowercase.
#     numhorasp12 = models.IntegerField(db_column='NumHorasP12', blank=True, null=True)  # Field name made lowercase.
#     m_dulo13 = models.CharField(db_column='M\xf3dulo13', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion13 = models.CharField(db_column='Descripcion13', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras13 = models.IntegerField(db_column='NumHoras13', blank=True, null=True)  # Field name made lowercase.
#     numhorasp13 = models.IntegerField(db_column='NumHorasP13', blank=True, null=True)  # Field name made lowercase.
#     m_dulo14 = models.CharField(db_column='M\xf3dulo14', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion14 = models.CharField(db_column='Descripcion14', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras14 = models.IntegerField(db_column='NumHoras14', blank=True, null=True)  # Field name made lowercase.
#     numhorasp14 = models.IntegerField(db_column='NumHorasP14', blank=True, null=True)  # Field name made lowercase.
#     m_dulo15 = models.CharField(db_column='M\xf3dulo15', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion15 = models.CharField(db_column='Descripcion15', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras15 = models.IntegerField(db_column='NumHoras15', blank=True, null=True)  # Field name made lowercase.
#     numhorasp15 = models.IntegerField(db_column='NumHorasP15', blank=True, null=True)  # Field name made lowercase.
#     m_dulo16 = models.CharField(db_column='M\xf3dulo16', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion16 = models.CharField(db_column='Descripcion16', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras16 = models.IntegerField(db_column='NumHoras16', blank=True, null=True)  # Field name made lowercase.
#     numhorasp16 = models.IntegerField(db_column='NumHorasP16', blank=True, null=True)  # Field name made lowercase.
#     m_dulo17 = models.CharField(db_column='M\xf3dulo17', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion17 = models.CharField(db_column='Descripcion17', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras17 = models.IntegerField(db_column='NumHoras17', blank=True, null=True)  # Field name made lowercase.
#     numhorasp17 = models.IntegerField(db_column='NumHorasP17', blank=True, null=True)  # Field name made lowercase.
#     m_dulo18 = models.CharField(db_column='M\xf3dulo18', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion18 = models.CharField(db_column='Descripcion18', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras18 = models.IntegerField(db_column='NumHoras18', blank=True, null=True)  # Field name made lowercase.
#     numhorasp18 = models.IntegerField(db_column='NumHorasP18', blank=True, null=True)  # Field name made lowercase.
#     m_dulo19 = models.CharField(db_column='M\xf3dulo19', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion19 = models.CharField(db_column='Descripcion19', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras19 = models.IntegerField(db_column='NumHoras19', blank=True, null=True)  # Field name made lowercase.
#     numhorasp19 = models.IntegerField(db_column='NumHorasP19', blank=True, null=True)  # Field name made lowercase.
#     m_dulo20 = models.CharField(db_column='M\xf3dulo20', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion20 = models.CharField(db_column='Descripcion20', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras20 = models.IntegerField(db_column='NumHoras20', blank=True, null=True)  # Field name made lowercase.
#     numhorasp20 = models.IntegerField(db_column='NumHorasP20', blank=True, null=True)  # Field name made lowercase.
#     formacionformadores = models.NullBooleanField(db_column='FormacionFormadores')  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#     m_dulo21 = models.CharField(db_column='M\xf3dulo21', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion21 = models.CharField(db_column='Descripcion21', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras21 = models.IntegerField(db_column='NumHoras21', blank=True, null=True)  # Field name made lowercase.
#     numhorasp21 = models.IntegerField(db_column='NumHorasP21', blank=True, null=True)  # Field name made lowercase.
#     m_dulo22 = models.CharField(db_column='M\xf3dulo22', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion22 = models.CharField(db_column='Descripcion22', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras22 = models.IntegerField(db_column='NumHoras22', blank=True, null=True)  # Field name made lowercase.
#     numhorasp22 = models.IntegerField(db_column='NumHorasP22', blank=True, null=True)  # Field name made lowercase.
#     m_dulo23 = models.CharField(db_column='M\xf3dulo23', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion23 = models.CharField(db_column='Descripcion23', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras23 = models.IntegerField(db_column='NumHoras23', blank=True, null=True)  # Field name made lowercase.
#     numhorasp23 = models.IntegerField(db_column='NumHorasP23', blank=True, null=True)  # Field name made lowercase.
#     m_dulo24 = models.CharField(db_column='M\xf3dulo24', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion24 = models.CharField(db_column='Descripcion24', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras24 = models.IntegerField(db_column='NumHoras24', blank=True, null=True)  # Field name made lowercase.
#     numhorasp24 = models.IntegerField(db_column='NumHorasP24', blank=True, null=True)  # Field name made lowercase.
#     m_dulo25 = models.CharField(db_column='M\xf3dulo25', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion25 = models.CharField(db_column='Descripcion25', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras25 = models.IntegerField(db_column='NumHoras25', blank=True, null=True)  # Field name made lowercase.
#     numhorasp25 = models.IntegerField(db_column='NumHorasP25', blank=True, null=True)  # Field name made lowercase.
#     m_dulo26 = models.CharField(db_column='M\xf3dulo26', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion26 = models.CharField(db_column='Descripcion26', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras26 = models.IntegerField(db_column='NumHoras26', blank=True, null=True)  # Field name made lowercase.
#     numhorasp26 = models.IntegerField(db_column='NumHorasP26', blank=True, null=True)  # Field name made lowercase.
#     m_dulo27 = models.CharField(db_column='M\xf3dulo27', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion27 = models.CharField(db_column='Descripcion27', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras27 = models.IntegerField(db_column='NumHoras27', blank=True, null=True)  # Field name made lowercase.
#     numhorasp27 = models.IntegerField(db_column='NumHorasP27', blank=True, null=True)  # Field name made lowercase.
#     m_dulo28 = models.CharField(db_column='M\xf3dulo28', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion28 = models.CharField(db_column='Descripcion28', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras28 = models.IntegerField(db_column='NumHoras28', blank=True, null=True)  # Field name made lowercase.
#     numhorasp28 = models.IntegerField(db_column='NumHorasP28', blank=True, null=True)  # Field name made lowercase.
#     m_dulo29 = models.CharField(db_column='M\xf3dulo29', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion29 = models.CharField(db_column='Descripcion29', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras29 = models.IntegerField(db_column='NumHoras29', blank=True, null=True)  # Field name made lowercase.
#     numhorasp29 = models.IntegerField(db_column='NumHorasP29', blank=True, null=True)  # Field name made lowercase.
#     m_dulo30 = models.CharField(db_column='M\xf3dulo30', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripcion30 = models.CharField(db_column='Descripcion30', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     numhoras30 = models.IntegerField(db_column='NumHoras30', blank=True, null=True)  # Field name made lowercase.
#     numhorasp30 = models.IntegerField(db_column='NumHorasP30', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'OfertaEducativa'
#
#
# class OfertaeducativaTombstone(models.Model):
#     clave = models.CharField(db_column='Clave', primary_key=True, max_length=20)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'OfertaEducativa_Tombstone'
#
#
# class Personas(models.Model):
#     numero_identidad = models.CharField(db_column='Numero_identidad', primary_key=True, max_length=15)  # Field name made lowercase.
#     nombre_completo = models.CharField(db_column='Nombre_Completo', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     fecha_de_nacimiento = models.DateTimeField(db_column='Fecha_de_Nacimiento', blank=True, null=True)  # Field name made lowercase.
#     edadentroprogramaa_os = models.IntegerField(db_column='EdadEntroProgramaA\xf1os', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     edadentroprogramameses = models.IntegerField(db_column='EdadEntroProgramaMeses', blank=True, null=True)  # Field name made lowercase.
#     sexo = models.CharField(db_column='Sexo', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     zona = models.CharField(db_column='Zona', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bloque = models.CharField(db_column='Bloque', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     referencia_direccion = models.TextField(db_column='Referencia_Direccion', blank=True, null=True)  # Field name made lowercase.
#     numero_de_casa = models.CharField(db_column='Numero_de_Casa', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     mun = models.ForeignKey(Catmunicipios, models.DO_NOTHING, db_column='Mun_id', blank=True, null=True)  # Field name made lowercase.
#     aldea = models.IntegerField(db_column='Aldea', blank=True, null=True)  # Field name made lowercase.
#     caserio = models.IntegerField(db_column='Caserio', blank=True, null=True)  # Field name made lowercase.
#     tel_fono = models.CharField(db_column='Tel\xe9fono', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     celular = models.CharField(db_column='Celular', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ec = models.ForeignKey(Catestadocivil, models.DO_NOTHING, db_column='EC_Id', blank=True, null=True)  # Field name made lowercase.
#     numero_de_hijos_varones = models.IntegerField(db_column='Numero_de_Hijos_Varones', blank=True, null=True)  # Field name made lowercase.
#     numero_hijas_hembras = models.IntegerField(db_column='Numero_Hijas_Hembras', blank=True, null=True)  # Field name made lowercase.
#     numero_de_dependientes = models.IntegerField(db_column='Numero_de_Dependientes', blank=True, null=True)  # Field name made lowercase.
#     ocupacionconyuge = models.CharField(db_column='OcupacionConyuge', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     ne = models.ForeignKey(Catniveleducativo, models.DO_NOTHING, db_column='NE_Id', blank=True, null=True)  # Field name made lowercase.
#     grado_alcanzado = models.CharField(db_column='Grado_Alcanzado', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trabaja_actualmente = models.NullBooleanField(db_column='Trabaja_Actualmente')  # Field name made lowercase.
#     tipo_institucion_en_que_labora = models.IntegerField(db_column='Tipo_Institucion_en_que_labora', blank=True, null=True)  # Field name made lowercase.
#     trabajo_anterior = models.CharField(db_column='Trabajo_Anterior', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tipo_institucion_ut = models.CharField(db_column='Tipo_Institucion_UT', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     expectativas = models.TextField(db_column='Expectativas', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
#     nac = models.ForeignKey(Catnacionalidad, models.DO_NOTHING, db_column='NAC_Id', blank=True, null=True)  # Field name made lowercase.
#     et = models.ForeignKey(Catetnias, models.DO_NOTHING, db_column='Et_Id', blank=True, null=True)  # Field name made lowercase.
#     rubro = models.CharField(db_column='Rubro', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     caja_rural = models.NullBooleanField(db_column='Caja_Rural')  # Field name made lowercase.
#     cooperativa = models.NullBooleanField(db_column='Cooperativa')  # Field name made lowercase.
#     junta_de_agua = models.NullBooleanField(db_column='Junta_de_Agua')  # Field name made lowercase.
#     patronato = models.NullBooleanField(db_column='Patronato')  # Field name made lowercase.
#     microempresas = models.NullBooleanField(db_column='Microempresas')  # Field name made lowercase.
#     otro = models.NullBooleanField(db_column='Otro')  # Field name made lowercase.
#     especifique = models.CharField(db_column='Especifique', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     idresponsable1 = models.CharField(db_column='IdResponsable1', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     nombrereposnsable1 = models.CharField(db_column='NombreReposnsable1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ocupacionresponsable1 = models.CharField(db_column='OcupacionResponsable1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nivelacademicoresponsable1 = models.IntegerField(db_column='NivelAcademicoResponsable1', blank=True, null=True)  # Field name made lowercase.
#     parentesco1 = models.CharField(db_column='Parentesco1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     idresponsable2 = models.CharField(db_column='IdResponsable2', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     nombrereposnsable2 = models.CharField(db_column='NombreReposnsable2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ocupacionresponsable2 = models.CharField(db_column='OcupacionResponsable2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nivelacademicoresponsable2 = models.IntegerField(db_column='NivelAcademicoResponsable2', blank=True, null=True)  # Field name made lowercase.
#     parentesco2 = models.CharField(db_column='Parentesco2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Personas'
#
#
# class Personasporprocesoeducativo(models.Model):
#     claveev = models.ForeignKey('Procesoseducativos', models.DO_NOTHING, db_column='ClaveEV')  # Field name made lowercase.
#     numero_identidad = models.CharField(db_column='Numero_identidad', max_length=15)  # Field name made lowercase.
#     pxp_id = models.IntegerField(db_column='PxP_Id', blank=True, null=True)  # Field name made lowercase.
#     ev_id = models.IntegerField(db_column='EV_Id', blank=True, null=True)  # Field name made lowercase.
#     per_id = models.IntegerField(db_column='Per_Id', blank=True, null=True)  # Field name made lowercase.
#     deserto = models.NullBooleanField(db_column='Deserto')  # Field name made lowercase.
#     fechadesercion = models.CharField(db_column='FechaDesercion', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     causappaldesercion = models.IntegerField(db_column='CausaPpalDesercion', blank=True, null=True)  # Field name made lowercase.
#     obscecap = models.TextField(db_column='ObsCECAP', blank=True, null=True)  # Field name made lowercase.
#     fuesometidoacertificacion = models.NullBooleanField(db_column='FueSometidoACertificacion')  # Field name made lowercase.
#     secertifico = models.NullBooleanField(db_column='SeCertifico')  # Field name made lowercase.
#     tipocertificado = models.IntegerField(db_column='TipoCertificado', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
#     edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'PersonasPorProcesoEducativo'
#         unique_together = (('claveev', 'numero_identidad'),)
#
#
# class PersonasporprocesoeducativoTombstone(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', max_length=20)  # Field name made lowercase.
#     numero_identidad = models.CharField(db_column='Numero_identidad', max_length=15)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'PersonasPorProcesoEducativo_Tombstone'
#         unique_together = (('claveev', 'numero_identidad'),)
#
#
# class PersonasTombstone(models.Model):
#     numero_identidad = models.CharField(db_column='Numero_identidad', primary_key=True, max_length=15)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Personas_Tombstone'
#
#
# class Procesoseducativos(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', primary_key=True, max_length=20)  # Field name made lowercase.
#     clave = models.ForeignKey(Ofertaeducativa, models.DO_NOTHING, db_column='Clave', blank=True, null=True)  # Field name made lowercase.
#     ev_nombre = models.CharField(db_column='EV_Nombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
#     ev_fechainicial = models.DateTimeField(db_column='EV_FechaInicial', blank=True, null=True)  # Field name made lowercase.
#     ev_fechafinal = models.DateTimeField(db_column='EV_FechaFinal', blank=True, null=True)  # Field name made lowercase.
#     totalhoras = models.FloatField(db_column='TotalHoras', blank=True, null=True)  # Field name made lowercase.
#     cd_id = models.IntegerField(db_column='CD_Id', blank=True, null=True)  # Field name made lowercase.
#     ev_lugar = models.CharField(db_column='EV_Lugar', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ed_id = models.IntegerField(db_column='Ed_Id', blank=True, null=True)  # Field name made lowercase.
#     alimentacion = models.NullBooleanField(db_column='Alimentacion')  # Field name made lowercase.
#     transporte = models.NullBooleanField(db_column='Transporte')  # Field name made lowercase.
#     hospedaje = models.NullBooleanField(db_column='Hospedaje')  # Field name made lowercase.
#     facilitador = models.NullBooleanField(db_column='Facilitador')  # Field name made lowercase.
#     materiales = models.NullBooleanField(db_column='Materiales')  # Field name made lowercase.
#     convocatoria = models.NullBooleanField(db_column='Convocatoria')  # Field name made lowercase.
#     fechacert = models.DateTimeField(db_column='FechaCert', blank=True, null=True)  # Field name made lowercase.
#     fechainiciomod1 = models.DateTimeField(db_column='Fechainiciomod1', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod1 = models.DateTimeField(db_column='Fechafinalmod1', blank=True, null=True)  # Field name made lowercase.
#     instructormod1 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod1', blank=True, null=True)
#     fechainiciomod2 = models.DateTimeField(db_column='Fechainiciomod2', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod2 = models.DateTimeField(db_column='Fechafinalmod2', blank=True, null=True)  # Field name made lowercase.
#     instructormod2 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod2', blank=True, null=True)
#     fechainiciomod3 = models.DateTimeField(db_column='Fechainiciomod3', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod3 = models.DateTimeField(db_column='Fechafinalmod3', blank=True, null=True)  # Field name made lowercase.
#     instructormod3 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod3', blank=True, null=True)
#     fechainiciomod4 = models.DateTimeField(db_column='Fechainiciomod4', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod4 = models.DateTimeField(db_column='Fechafinalmod4', blank=True, null=True)  # Field name made lowercase.
#     instructormod4 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod4', blank=True, null=True)
#     fechainiciomod5 = models.DateTimeField(db_column='Fechainiciomod5', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod5 = models.DateTimeField(db_column='Fechafinalmod5', blank=True, null=True)  # Field name made lowercase.
#     instructormod5 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod5', blank=True, null=True)
#     fechainiciomod6 = models.DateTimeField(db_column='Fechainiciomod6', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod6 = models.DateTimeField(db_column='Fechafinalmod6', blank=True, null=True)  # Field name made lowercase.
#     instructormod6 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod6', blank=True, null=True)
#     fechainiciomod7 = models.DateTimeField(db_column='Fechainiciomod7', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod7 = models.DateTimeField(db_column='Fechafinalmod7', blank=True, null=True)  # Field name made lowercase.
#     instructormod7 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod7', blank=True, null=True)
#     fechainiciomod8 = models.DateTimeField(db_column='Fechainiciomod8', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod8 = models.DateTimeField(db_column='Fechafinalmod8', blank=True, null=True)  # Field name made lowercase.
#     instructormod8 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod8', blank=True, null=True)
#     fechainiciomod9 = models.DateTimeField(db_column='Fechainiciomod9', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod9 = models.DateTimeField(db_column='Fechafinalmod9', blank=True, null=True)  # Field name made lowercase.
#     instructormod9 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod9', blank=True, null=True)
#     fechainiciomod10 = models.DateTimeField(db_column='Fechainiciomod10', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod10 = models.DateTimeField(db_column='Fechafinalmod10', blank=True, null=True)  # Field name made lowercase.
#     instructormod10 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod10', blank=True, null=True)
#     fechainiciomod11 = models.DateTimeField(db_column='Fechainiciomod11', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod11 = models.DateTimeField(db_column='Fechafinalmod11', blank=True, null=True)  # Field name made lowercase.
#     instructormod11 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod11', blank=True, null=True)
#     fechainiciomod12 = models.DateTimeField(db_column='Fechainiciomod12', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod12 = models.DateTimeField(db_column='Fechafinalmod12', blank=True, null=True)  # Field name made lowercase.
#     instructormod12 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod12', blank=True, null=True)
#     fechainiciomod13 = models.DateTimeField(db_column='Fechainiciomod13', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod13 = models.DateTimeField(db_column='Fechafinalmod13', blank=True, null=True)  # Field name made lowercase.
#     instructormod13 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod13', blank=True, null=True)
#     fechainiciomod14 = models.DateTimeField(db_column='Fechainiciomod14', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod14 = models.DateTimeField(db_column='Fechafinalmod14', blank=True, null=True)  # Field name made lowercase.
#     instructormod14 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod14', blank=True, null=True)
#     fechainiciomod15 = models.DateTimeField(db_column='Fechainiciomod15', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod15 = models.DateTimeField(db_column='Fechafinalmod15', blank=True, null=True)  # Field name made lowercase.
#     instructormod15 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod15', blank=True, null=True)
#     fechainiciomod16 = models.DateTimeField(db_column='Fechainiciomod16', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod16 = models.DateTimeField(db_column='Fechafinalmod16', blank=True, null=True)  # Field name made lowercase.
#     instructormod16 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod16', blank=True, null=True)
#     fechainiciomod17 = models.DateTimeField(db_column='Fechainiciomod17', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod17 = models.DateTimeField(db_column='Fechafinalmod17', blank=True, null=True)  # Field name made lowercase.
#     instructormod17 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod17', blank=True, null=True)
#     fechainiciomod18 = models.DateTimeField(db_column='Fechainiciomod18', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod18 = models.DateTimeField(db_column='Fechafinalmod18', blank=True, null=True)  # Field name made lowercase.
#     instructormod18 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod18', blank=True, null=True)
#     fechainiciomod19 = models.DateTimeField(db_column='Fechainiciomod19', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod19 = models.DateTimeField(db_column='Fechafinalmod19', blank=True, null=True)  # Field name made lowercase.
#     instructormod19 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod19', blank=True, null=True)
#     fechainiciomod20 = models.DateTimeField(db_column='Fechainiciomod20', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod20 = models.DateTimeField(db_column='Fechafinalmod20', blank=True, null=True)  # Field name made lowercase.
#     instructormod20 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod20', blank=True, null=True)
#     tipomaterial = models.ForeignKey(Catmaterialdidactico, models.DO_NOTHING, db_column='TipoMaterial', blank=True, null=True)  # Field name made lowercase.
#     metodologia = models.IntegerField(db_column='Metodologia', blank=True, null=True)  # Field name made lowercase.
#     metodologiatxt = models.CharField(db_column='MetodologiaTXT', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     modalidad = models.ForeignKey(Catmodalidades, models.DO_NOTHING, db_column='Modalidad', blank=True, null=True)  # Field name made lowercase.
#     tipomodalidad = models.ForeignKey(Cattipomodalidad, models.DO_NOTHING, db_column='TipoModalidad')  # Field name made lowercase.
#     opcioneducativa = models.ForeignKey(Catopcioneseducativas, models.DO_NOTHING, db_column='OpcionEducativa', blank=True, null=True)  # Field name made lowercase.
#     sectoreconomico = models.IntegerField(db_column='SectorEconomico', blank=True, null=True)  # Field name made lowercase.
#     proyectoid = models.ForeignKey('Proyectos', models.DO_NOTHING, db_column='ProyectoId', blank=True, null=True)  # Field name made lowercase.
#     tipocalificacion = models.IntegerField(db_column='TipoCalificacion', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#     fechainiciomod21 = models.DateTimeField(db_column='Fechainiciomod21', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod21 = models.DateTimeField(db_column='Fechafinalmod21', blank=True, null=True)  # Field name made lowercase.
#     instructormod21 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod22 = models.DateTimeField(db_column='Fechainiciomod22', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod22 = models.DateTimeField(db_column='Fechafinalmod22', blank=True, null=True)  # Field name made lowercase.
#     instructormod22 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod23 = models.DateTimeField(db_column='Fechainiciomod23', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod23 = models.DateTimeField(db_column='Fechafinalmod23', blank=True, null=True)  # Field name made lowercase.
#     instructormod23 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod24 = models.DateTimeField(db_column='Fechainiciomod24', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod24 = models.DateTimeField(db_column='Fechafinalmod24', blank=True, null=True)  # Field name made lowercase.
#     instructormod24 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod25 = models.DateTimeField(db_column='Fechainiciomod25', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod25 = models.DateTimeField(db_column='Fechafinalmod25', blank=True, null=True)  # Field name made lowercase.
#     instructormod25 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod26 = models.DateTimeField(db_column='Fechainiciomod26', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod26 = models.DateTimeField(db_column='Fechafinalmod26', blank=True, null=True)  # Field name made lowercase.
#     instructormod26 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod27 = models.DateTimeField(db_column='Fechainiciomod27', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod27 = models.DateTimeField(db_column='Fechafinalmod27', blank=True, null=True)  # Field name made lowercase.
#     instructormod27 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod28 = models.DateTimeField(db_column='Fechainiciomod28', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod28 = models.DateTimeField(db_column='Fechafinalmod28', blank=True, null=True)  # Field name made lowercase.
#     instructormod28 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod29 = models.DateTimeField(db_column='Fechainiciomod29', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod29 = models.DateTimeField(db_column='Fechafinalmod29', blank=True, null=True)  # Field name made lowercase.
#     instructormod29 = models.CharField(max_length=20, blank=True, null=True)
#     fechainiciomod30 = models.DateTimeField(db_column='Fechainiciomod30', blank=True, null=True)  # Field name made lowercase.
#     fechafinalmod30 = models.DateTimeField(db_column='Fechafinalmod30', blank=True, null=True)  # Field name made lowercase.
#     instructormod30 = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ProcesosEducativos'
#
#
# class ProcesoseducativosTombstone(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', primary_key=True, max_length=20)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'ProcesosEducativos_Tombstone'
#
#
# class Proyectos(models.Model):
#     proyectoid = models.CharField(db_column='ProyectoId', primary_key=True, max_length=20)  # Field name made lowercase.
#     proyectonombre = models.CharField(db_column='ProyectoNombre', max_length=200)  # Field name made lowercase.
#     proyectoobjetivo = models.TextField(db_column='ProyectoObjetivo')  # Field name made lowercase.
#     proyectopresupuestoconeanfo = models.DecimalField(db_column='ProyectoPresupuestoConeanfo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     proyectofechainicio = models.CharField(db_column='ProyectoFechaInicio', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     proyectofechafinal = models.CharField(db_column='ProyectoFechaFinal', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     donante = models.CharField(db_column='Donante', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Proyectos'
#
#
# class ProyectosTombstone(models.Model):
#     proyectoid = models.CharField(db_column='ProyectoId', primary_key=True, max_length=20)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Proyectos_Tombstone'
#
#
# class Solicitudescert(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', primary_key=True, max_length=20)  # Field name made lowercase.
#     idsolicitud = models.AutoField(db_column='idSolicitud')  # Field name made lowercase.
#     ev_id = models.IntegerField(db_column='EV_Id', blank=True, null=True)  # Field name made lowercase.
#     fechapropuestacert = models.CharField(db_column='FechaPropuestaCert', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     comentariosadicionales = models.TextField(db_column='ComentariosAdicionales', blank=True, null=True)  # Field name made lowercase.
#     solicitudestatus = models.CharField(db_column='SolicitudEstatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     razonescancelacion = models.TextField(db_column='RazonesCancelacion', blank=True, null=True)  # Field name made lowercase.
#     fechasolicitud = models.CharField(db_column='FechaSolicitud', max_length=27, blank=True, null=True)  # Field name made lowercase.
#     solicitudaceptada = models.IntegerField(db_column='SolicitudAceptada', blank=True, null=True)  # Field name made lowercase.
#     razonesrechazo = models.TextField(db_column='RazonesRechazo', blank=True, null=True)  # Field name made lowercase.
#     pruebaaplicar = models.IntegerField(db_column='PruebaAplicar', blank=True, null=True)  # Field name made lowercase.
#     evaluador = models.IntegerField(db_column='Evaluador', blank=True, null=True)  # Field name made lowercase.
#     fechaconsensuada = models.CharField(db_column='FechaConsensuada', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     lugar = models.TextField(db_column='Lugar', blank=True, null=True)  # Field name made lowercase.
#     otrasdisposiciones = models.TextField(db_column='OtrasDisposiciones', blank=True, null=True)  # Field name made lowercase.
#     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'SolicitudesCert'
#
#
# class SolicitudescertTombstone(models.Model):
#     claveev = models.CharField(db_column='ClaveEV', primary_key=True, max_length=20)  # Field name made lowercase.
#     deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'SolicitudesCert_Tombstone'
#
#
# class AspnetApplications(models.Model):
#     applicationname = models.CharField(db_column='ApplicationName', unique=True, max_length=256)  # Field name made lowercase.
#     loweredapplicationname = models.CharField(db_column='LoweredApplicationName', unique=True, max_length=256)  # Field name made lowercase.
#     applicationid = models.CharField(db_column='ApplicationId', primary_key=True, max_length=36)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_Applications'
#
#
# class AspnetMembership(models.Model):
#     applicationid = models.ForeignKey(AspnetApplications, models.DO_NOTHING, db_column='ApplicationId')  # Field name made lowercase.
#     userid = models.ForeignKey('AspnetUsers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=128)  # Field name made lowercase.
#     passwordformat = models.IntegerField(db_column='PasswordFormat')  # Field name made lowercase.
#     passwordsalt = models.CharField(db_column='PasswordSalt', max_length=128)  # Field name made lowercase.
#     mobilepin = models.CharField(db_column='MobilePIN', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     loweredemail = models.CharField(db_column='LoweredEmail', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     passwordquestion = models.CharField(db_column='PasswordQuestion', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     passwordanswer = models.CharField(db_column='PasswordAnswer', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     isapproved = models.BooleanField(db_column='IsApproved')  # Field name made lowercase.
#     islockedout = models.BooleanField(db_column='IsLockedOut')  # Field name made lowercase.
#     createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
#     lastlogindate = models.DateTimeField(db_column='LastLoginDate')  # Field name made lowercase.
#     lastpasswordchangeddate = models.DateTimeField(db_column='LastPasswordChangedDate')  # Field name made lowercase.
#     lastlockoutdate = models.DateTimeField(db_column='LastLockoutDate')  # Field name made lowercase.
#     failedpasswordattemptcount = models.IntegerField(db_column='FailedPasswordAttemptCount')  # Field name made lowercase.
#     failedpasswordattemptwindowstart = models.DateTimeField(db_column='FailedPasswordAttemptWindowStart')  # Field name made lowercase.
#     failedpasswordanswerattemptcount = models.IntegerField(db_column='FailedPasswordAnswerAttemptCount')  # Field name made lowercase.
#     failedpasswordanswerattemptwindowstart = models.DateTimeField(db_column='FailedPasswordAnswerAttemptWindowStart')  # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_Membership'
#
#
# class AspnetPaths(models.Model):
#     applicationid = models.ForeignKey(AspnetApplications, models.DO_NOTHING, db_column='ApplicationId')  # Field name made lowercase.
#     pathid = models.CharField(db_column='PathId', primary_key=True, max_length=36)  # Field name made lowercase.
#     path = models.CharField(db_column='Path', max_length=256)  # Field name made lowercase.
#     loweredpath = models.CharField(db_column='LoweredPath', max_length=256)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_Paths'
#         unique_together = (('applicationid', 'loweredpath'),)
#
#
# class AspnetPersonalizationallusers(models.Model):
#     pathid = models.ForeignKey(AspnetPaths, models.DO_NOTHING, db_column='PathId', primary_key=True)  # Field name made lowercase.
#     pagesettings = models.BinaryField(db_column='PageSettings')  # Field name made lowercase.
#     lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_PersonalizationAllUsers'
#
#
# class AspnetPersonalizationperuser(models.Model):
#     id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
#     pathid = models.ForeignKey(AspnetPaths, models.DO_NOTHING, db_column='PathId', blank=True, null=True)  # Field name made lowercase.
#     userid = models.ForeignKey('AspnetUsers', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
#     pagesettings = models.BinaryField(db_column='PageSettings')  # Field name made lowercase.
#     lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_PersonalizationPerUser'
#         unique_together = (('pathid', 'userid'), ('userid', 'pathid'),)
#
#
# class AspnetProfile(models.Model):
#     userid = models.ForeignKey('AspnetUsers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
#     propertynames = models.TextField(db_column='PropertyNames')  # Field name made lowercase.
#     propertyvaluesstring = models.TextField(db_column='PropertyValuesString')  # Field name made lowercase.
#     propertyvaluesbinary = models.BinaryField(db_column='PropertyValuesBinary')  # Field name made lowercase.
#     lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_Profile'
#
#
# class AspnetRoles(models.Model):
#     applicationid = models.ForeignKey(AspnetApplications, models.DO_NOTHING, db_column='ApplicationId')  # Field name made lowercase.
#     roleid = models.CharField(db_column='RoleId', primary_key=True, max_length=36)  # Field name made lowercase.
#     rolename = models.CharField(db_column='RoleName', max_length=256)  # Field name made lowercase.
#     loweredrolename = models.CharField(db_column='LoweredRoleName', max_length=256)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_Roles'
#         unique_together = (('applicationid', 'loweredrolename'),)
#
#
# class AspnetSchemaversions(models.Model):
#     feature = models.CharField(db_column='Feature', max_length=128)  # Field name made lowercase.
#     compatibleschemaversion = models.CharField(db_column='CompatibleSchemaVersion', max_length=128)  # Field name made lowercase.
#     iscurrentversion = models.BooleanField(db_column='IsCurrentVersion')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_SchemaVersions'
#         unique_together = (('feature', 'compatibleschemaversion'),)
#
#
# class AspnetUsers(models.Model):
#     applicationid = models.ForeignKey(AspnetApplications, models.DO_NOTHING, db_column='ApplicationId')  # Field name made lowercase.
#     userid = models.CharField(db_column='UserId', primary_key=True, max_length=36)  # Field name made lowercase.
#     username = models.CharField(db_column='UserName', max_length=256)  # Field name made lowercase.
#     loweredusername = models.CharField(db_column='LoweredUserName', max_length=256)  # Field name made lowercase.
#     mobilealias = models.CharField(db_column='MobileAlias', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     isanonymous = models.BooleanField(db_column='IsAnonymous')  # Field name made lowercase.
#     lastactivitydate = models.DateTimeField(db_column='LastActivityDate')  # Field name made lowercase.
#     clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_Users'
#         unique_together = (('applicationid', 'loweredusername'),)
#
#
# class AspnetUsersinroles(models.Model):
#     userid = models.ForeignKey(AspnetUsers, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
#     roleid = models.ForeignKey(AspnetRoles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_UsersInRoles'
#         unique_together = (('userid', 'roleid'),)
#
#
# class AspnetWebeventEvents(models.Model):
#     eventid = models.CharField(db_column='EventId', primary_key=True, max_length=32)  # Field name made lowercase.
#     eventtimeutc = models.DateTimeField(db_column='EventTimeUtc')  # Field name made lowercase.
#     eventtime = models.DateTimeField(db_column='EventTime')  # Field name made lowercase.
#     eventtype = models.CharField(db_column='EventType', max_length=256)  # Field name made lowercase.
#     eventsequence = models.DecimalField(db_column='EventSequence', max_digits=19, decimal_places=0)  # Field name made lowercase.
#     eventoccurrence = models.DecimalField(db_column='EventOccurrence', max_digits=19, decimal_places=0)  # Field name made lowercase.
#     eventcode = models.IntegerField(db_column='EventCode')  # Field name made lowercase.
#     eventdetailcode = models.IntegerField(db_column='EventDetailCode')  # Field name made lowercase.
#     message = models.CharField(db_column='Message', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     applicationpath = models.CharField(db_column='ApplicationPath', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     applicationvirtualpath = models.CharField(db_column='ApplicationVirtualPath', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     machinename = models.CharField(db_column='MachineName', max_length=256)  # Field name made lowercase.
#     requesturl = models.CharField(db_column='RequestUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     exceptiontype = models.CharField(db_column='ExceptionType', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aspnet_WebEvent_Events'
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
