from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Perfil(AbstractUser):
    clavecap=models.CharField(max_length=100)
    usuario = models.BooleanField(default=False)
    administrador = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

class Catclaseeducador(models.Model):
    cle_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    cle_claseeducador = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    lasteditdate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.cle_claseeducador


class Catdepartamentos(models.Model):
     dep_id = models.IntegerField(db_column='Dep_Id', primary_key=True)  # Field name made lowercase.
     dep_departamento = models.CharField(db_column='Dep_Departamento', max_length=50, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.dep_departamento

class Catmunicipios(models.Model):
     mun_id = models.IntegerField(db_column='Mun_Id', primary_key=True)  # Field name made lowercase.
     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
     mun_municipio = models.CharField(db_column='Mun_Municipio', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.mun_municipio


class Cataldeas(models.Model):
     idaldea = models.IntegerField(db_column='IdAldea', primary_key=True)  # Field name made lowercase.
     nombrealdea = models.CharField(db_column='NombreAldea', max_length=250, blank=True, null=True)  # Field name made lowercase.
     idmunicipio = models.ForeignKey('Catmunicipios', models.DO_NOTHING, db_column='IdMunicipio', blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.nombrealdea



class Catcaserios(models.Model):
    idcaserio = models.IntegerField(db_column='IdCaserio', primary_key=True)  # Field name made lowercase.
    nombrecaserio = models.CharField(db_column='NombreCaserio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idaldea = models.ForeignKey(Cataldeas, models.DO_NOTHING, db_column='IdAldea', blank=True, null=True)  # Field name made lowercase.
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.nombrecaserio

class Catcecaps(models.Model):
      cecap_id = models.AutoField(db_column='Cecap_Id',primary_key=True,)  # Field name made lowercase.
      cecap_nombre = models.CharField(db_column='Cecap_Nombre', max_length=100)  # Field name made lowercase.
      dep = models.ForeignKey('Catdepartamentos', db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
      mun = models.ForeignKey('Catmunicipios', db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
      cecap_direccion = models.TextField(db_column='Cecap_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
      cecap_telefono = models.CharField(db_column='Cecap_Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase.
      cecap_contacto = models.CharField(db_column='Cecap_Contacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
      cecap_emailcontacto = models.CharField(db_column='Cecap_EmailContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
      cecap_activo = models.NullBooleanField(db_column='Cecap_Activo')  # Field name made lowercase.
      cecap_fechafundacion = models.CharField(db_column='Cecap_FechaFundacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
      ue = models.ForeignKey('Catunidadesejecutoras', db_column='UE_Id', blank=True, null=True)  # Field name made lowercase.
      clavececap = models.CharField(db_column='ClaveCecap', max_length=10)  # Field name made lowercase.
      lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
      creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

      def __unicode__(self):
          return self.cecap_nombre


class Cattipoinstitucion(models.Model):
    ti_id = models.AutoField(db_column='TI_Id', primary_key=True)  # Field name made lowercase.
    ti_tipoinstitucion = models.CharField(db_column='TI_TipoInstitucion', max_length=100)  # Field name made lowercase.
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    #
    def __unicode__(self):
        return self.ti_tipoinstitucion

class Catunidadesejecutoras(models.Model):
     ue_id = models.AutoField(db_column='UE_Id', primary_key=True)  # Field name made lowercase.
     ue_nombre = models.CharField(db_column='UE_Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ti = models.ForeignKey(Cattipoinstitucion, models.DO_NOTHING, db_column='TI_Id', blank=True, null=True)  # Field name made lowercase.
     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
     mun = models.ForeignKey(Catmunicipios, models.DO_NOTHING, db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
     ue_direccion = models.TextField(db_column='UE_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
     ue_telefono1 = models.CharField(db_column='UE_Telefono1', max_length=10, blank=True, null=True)  # Field name made lowercase.
     ue_telefono2 = models.CharField(db_column='UE_Telefono2', max_length=10, blank=True, null=True)  # Field name made lowercase.
     ue_responsabletecnico = models.CharField(db_column='UE_ResponsableTecnico', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ue_cargoresponsabletecnico = models.CharField(db_column='UE_CargoResponsableTecnico', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ue_emailresponsabletecnico = models.CharField(db_column='UE_EmailResponsableTecnico', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ue_sitioweb = models.CharField(db_column='UE_SitioWEB', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ue_areainfluencia = models.TextField(db_column='UE_AreaInfluencia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
     ue_nombrecontacto = models.CharField(db_column='UE_NombreContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ue_cargocontacto = models.CharField(db_column='UE_CargoContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
     ue_emailcontacto = models.CharField(db_column='UE_EmailContacto', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
     def __unicode__(self):
         return self.ue_nombre


class Catmaterialdidactico(models.Model):
     md_id = models.AutoField(db_column='MD_Id', primary_key=True)  # Field name made lowercase.
     md_materialdidactico = models.CharField(db_column='MD_MaterialDidactico', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.md_materialdidactico


class Catmetodologia(models.Model):
     met_id = models.IntegerField(db_column='MET_Id', primary_key=True)  # Field name made lowercase.
     met_metodologia = models.CharField(db_column='MET_Metodologia', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.met_metodologia

class Catmodalidades(models.Model):
     mo_id = models.AutoField(db_column='MO_Id', primary_key=True)  # Field name made lowercase.
     mo_modalidades = models.CharField(db_column='MO_Modalidades', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.mo_modalidades


class Catopcioneseducativas(models.Model):
     oe_id = models.AutoField(db_column='OE_Id', primary_key=True)  # Field name made lowercase.
     oe_opcioneducativa = models.CharField(db_column='OE_OpcionEducativa', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.oe_opcioneducativa


class Cattipomodalidad(models.Model):
     tmod_id = models.AutoField(db_column='TMod_Id', primary_key=True)  # Field name made lowercase.
     modalidadid = models.ForeignKey(Catmodalidades, models.DO_NOTHING, db_column='ModalidadId', blank=True, null=True)  # Field name made lowercase.
     tmodo_tipomodalidad = models.CharField(db_column='TModo_TipoModalidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
     def __unicode__(self):
         return self.tmodo_tipomodalidad


class Cattiposadministracion(models.Model):
     ta_id = models.AutoField(db_column='TA_Id', primary_key=True)  # Field name made lowercase.
     ta_tipoadministracion = models.CharField(db_column='TA_TipoAdministracion', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
     def __unicode__(self):
         return self.ta_tipoadministracion

class Cattipossedes(models.Model):
     ts_id = models.AutoField(db_column='TS_Id', primary_key=True)  # Field name made lowercase.
     ts_tiposede = models.CharField(db_column='TS_TipoSede', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.ts_tiposede

class Catsectoreseconomicos(models.Model):
     se_id = models.AutoField(db_column='SE_Id', primary_key=True)  # Field name made lowercase.
     se_sectoreconomico = models.CharField(db_column='SE_SectorEconomico', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.se_sectoreconomico


class Catniveleducativo(models.Model):
     ne_id = models.AutoField(db_column='NE_Id', primary_key=True)  # Field name made lowercase.
     ne_niveleducativo = models.CharField(db_column='NE_NivelEducativo', max_length=100, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.ne_niveleducativo


class Catnacionalidad(models.Model):
     nac_id = models.AutoField(db_column='Nac_Id', primary_key=True)  # Field name made lowercase.
     nac_nacionalidad = models.CharField(db_column='Nac_Nacionalidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.nac_nacionalidad


class Catetnias(models.Model):
     et_id = models.AutoField(db_column='Et_Id', primary_key=True)  # Field name made lowercase.
     et_nombreetnia = models.CharField(db_column='Et_NombreEtnia', max_length=50)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.et_nombreetnia


class Catestadocivil(models.Model):
     ec_id = models.AutoField(db_column='EC_Id', primary_key=True)  # Field name made lowercase.
     ec_estadocivil = models.CharField(db_column='EC_EstadoCivil', max_length=50)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
     def __unicode__(self):
         return self.ec_estadocivil



class Cateducadores(models.Model):
    ed_id = models.CharField(db_column='Ed_Id', primary_key=True, max_length=20)  # Field name made lowercase.
    ed_nombreeducador = models.CharField(db_column='Ed_NombreEducador', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cle = models.ForeignKey(Catclaseeducador, models.DO_NOTHING, db_column='Cle_Id', blank=True, null=True)  # Field name made lowercase.
    ed_identidad = models.CharField(db_column='Ed_Identidad', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ed_sexo = models.CharField(db_column='Ed_Sexo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
    mun = models.ForeignKey('Catmunicipios', models.DO_NOTHING, db_column='Mun_Id', blank=True, null=True)  # Field name made lowercase.
    aldea = models.IntegerField(db_column='Aldea', blank=True, null=True)  # Field name made lowercase.
    caserio = models.IntegerField(db_column='Caserio', blank=True, null=True)  # Field name made lowercase.
    ed_direccion = models.TextField(db_column='Ed_Direccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ed_telefono = models.CharField(db_column='Ed_Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase.
    #ed_celular = models.CharField(db_column='Ed_Celular', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ed_correoelectronico = models.CharField(db_column='Ed_CorreoElectronico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    et = models.ForeignKey('Catetnias', models.DO_NOTHING, db_column='Et_Id', blank=True, null=True)  # Field name made lowercase.
    ne = models.ForeignKey('Catniveleducativo', models.DO_NOTHING, db_column='NE_Id', blank=True, null=True)  # Field name made lowercase.
    ed_gradoalcanzado = models.CharField(db_column='Ed_GradoAlcanzado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ec = models.ForeignKey('Catestadocivil', models.DO_NOTHING, db_column='EC_Id', blank=True, null=True)  # Field name made lowercase.
    nac = models.ForeignKey('Catnacionalidad', models.DO_NOTHING, db_column='Nac_Id', blank=True, null=True)  # Field name made lowercase.
    cecap_id = models.IntegerField(db_column='Cecap_Id', blank=True, null=True)  # Field name made lowercase.
    clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateTimeField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.ed_nombreeducador



class ProcesoEducativo(models.Model):
    cecap_id = models.IntegerField(db_column='Cecap_Id', blank=True, null=True)  # Field name made lowercase.
    clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clave = models.CharField(db_column='Clave', primary_key=True, max_length=20)  # Field name made lowercase.
    cd_id = models.IntegerField(db_column='CD_Id', blank=True, null=True)  # Field name made lowercase.
    Nombre_Proceso = models.CharField(db_column='CD_Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    Nombre_Salida = models.CharField(db_column='NombreSalida', max_length=100, blank=True, null=True)  # Field name made lowercase.
    Total_Horas = models.IntegerField(db_column='CD_TotalHoras', blank=True, null=True)  # Field name made lowercase.
    Proceso_Formacion = models.CharField(db_column='ProcesoFormacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Objetivo = models.CharField(db_column='Objetivo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ev_fechainicial = models.DateTimeField(db_column='EV_FechaInicial', blank=True,null=True)  # Field name made lowercase.
    ev_fechafinal = models.DateTimeField(db_column='EV_FechaFinal', blank=True, null=True)  # Field name made lowercase.
    dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
    mun = models.ForeignKey(Catmunicipios, models.DO_NOTHING, db_column='Mun_id', blank=True, null=True)  # Field name made lowercase.
    Donde_desarrollara_proceso = models.CharField(db_column='Donde_desarrollara_proceso', max_length=300, blank=True, null=True)  # Field name made lowercase.
    opcioneducativa = models.ForeignKey(Catopcioneseducativas, models.DO_NOTHING, db_column='OpcionEducativa', blank=True, null=True)  # Field name made lowercase.
    metodologiatxt = models.CharField(db_column='MetodologiaTXT', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tipomaterial = models.ForeignKey(Catmaterialdidactico, models.DO_NOTHING, db_column='TipoMaterial', blank=True, null=True)  # Field name made lowercase.
    modalidad = models.ForeignKey(Catmodalidades, models.DO_NOTHING, db_column='Modalidad', blank=True, null=True)  # Field name made lowercase.
    tipomodalidad = models.ForeignKey(Cattipomodalidad, models.DO_NOTHING, db_column='TipoModalidad')  # Field name made lowercase.
    sectoreconomico = models.IntegerField(db_column='SectorEconomico', blank=True, null=True)  # Field name made lowercase.
    proyectoid = models.ForeignKey('Proyectos', models.DO_NOTHING, db_column='ProyectoId', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return self.Nombre_Proceso




class Proyectos(models.Model):
    proyectoid = models.CharField(db_column='ProyectoId', primary_key=True, max_length=20)  # Field name made lowercase.
    proyectonombre = models.CharField(db_column='ProyectoNombre', max_length=200)  # Field name made lowercase.
    proyectoobjetivo = models.TextField(db_column='ProyectoObjetivo')  # Field name made lowercase.
    proyectopresupuestoconeanfo = models.DecimalField(db_column='ProyectoPresupuestoConeanfo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    proyectofechainicio = models.CharField(db_column='ProyectoFechaInicio', max_length=10, blank=True, null=True)  # Field name made lowercase.
    proyectofechafinal = models.CharField(db_column='ProyectoFechaFinal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    donante = models.CharField(db_column='Donante', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.proyectonombre

class Personas(models.Model):
     id_personas=models.AutoField(db_column='id_personas' ,primary_key=True,)
     clavececap = models.CharField(db_column='ClaveCecap', max_length=10, blank=True, null=True)  # Field name made lowercase.
     numero_identidad = models.CharField(db_column='Numero_identidad', max_length=13)  # Field name made lowercase.
     nombre_completo = models.CharField(db_column='Nombre_Completo', max_length=33, blank=True, null=True)  # Field name made lowercase.
     fecha_de_nacimiento = models.DateTimeField(db_column='Fecha_de_Nacimiento', blank=True, null=True)  # Field name made lowercase.
     edadentroprogramaa_os = models.CharField(db_column='EdadEntroProgramaAnos', max_length=300 ,blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
     edadentroprogramameses = models.CharField(db_column='EdadEntroProgramaMeses',max_length=300, blank=True, null=True)  # Field name made lowercase.
     sexo = models.CharField(db_column='Sexo', max_length=20, blank=True, null=True)  # Field name made lowercase.
     domicilio = models.CharField(db_column='Zona', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bloque = models.CharField(db_column='Bloque', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     referencia_direccion = models.TextField(db_column='Referencia_Direccion', blank=True, null=True)  # Field name made lowercase.
#     numero_de_casa = models.CharField(db_column='Numero_de_Casa', max_length=10, blank=True, null=True)  # Field name made lowercase.
     dep = models.ForeignKey(Catdepartamentos, models.DO_NOTHING, db_column='Dep_Id', blank=True, null=True)  # Field name made lowercase.
     mun = models.ForeignKey(Catmunicipios, models.DO_NOTHING, db_column='Mun_id', blank=True, null=True)  # Field name made lowercase.
     aldea = models.IntegerField(db_column='Aldea', blank=True, null=True)  # Field name made lowercase.
     caserio = models.IntegerField(db_column='Caserio', blank=True, null=True)  # Field name made lowercase.
     tel_fono = models.CharField(db_column='Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
     ec = models.ForeignKey(Catestadocivil, models.DO_NOTHING, db_column='EC_Id', blank=True, null=True)  # Field name made lowercase.
     esta_estudiando = models.IntegerField(db_column='EstaEstudiando', blank=True, null=True)  # Field name made lowercase.
     tiene_alguna_discapacidad = models.IntegerField(db_column='Tiene_Alguna_Discapacidad', blank=True, null=True)  # Field name made lowercase.
#     numero_de_dependientes = models.IntegerField(db_column='Numero_de_Dependientes', blank=True, null=True)  # Field name made lowercase.
#     ocupacionconyuge = models.CharField(db_column='OcupacionConyuge', max_length=150, blank=True, null=True)  # Field name made lowercase.
     ne = models.ForeignKey(Catniveleducativo, models.DO_NOTHING, db_column='NE_Id', blank=True, null=True)  # Field name made lowercase.
     grado_alcanzado = models.CharField(db_column='Grado_Alcanzado', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trabaja_actualmente = models.NullBooleanField(db_column='Trabaja_Actualmente')  # Field name made lowercase.
#     tipo_institucion_en_que_labora = models.IntegerField(db_column='Tipo_Institucion_en_que_labora', blank=True, null=True)  # Field name made lowercase.
#     trabajo_anterior = models.CharField(db_column='Trabajo_Anterior', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tipo_institucion_ut = models.CharField(db_column='Tipo_Institucion_UT', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     expectativas = models.TextField(db_column='Expectativas', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
#     nac = models.ForeignKey(Catnacionalidad, models.DO_NOTHING, db_column='NAC_Id', blank=True, null=True)  # Field name made lowercase.
     et = models.ForeignKey(Catetnias, models.DO_NOTHING, db_column='Et_Id', blank=True, null=True)  # Field name made lowercase.
#     rubro = models.CharField(db_column='Rubro', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     caja_rural = models.NullBooleanField(db_column='Caja_Rural')  # Field name made lowercase.
#     cooperativa = models.NullBooleanField(db_column='Cooperativa')  # Field name made lowercase.
#     junta_de_agua = models.NullBooleanField(db_column='Junta_de_Agua')  # Field name made lowercase.
#     patronato = models.NullBooleanField(db_column='Patronato')  # Field name made lowercase.
#     microempresas = models.NullBooleanField(db_column='Microempresas')  # Field name made lowercase.
#     otro = models.NullBooleanField(db_column='Otro')  # Field name made lowercase.
#     especifique = models.CharField(db_column='Especifique', max_length=50, blank=True, null=True)  # Field name made lowercase.
     nombrereposnsable1 = models.CharField(db_column='NombreReposnsable1', max_length=50, blank=True, null=True)  # Field name made lowercase.
     idresponsable1 = models.CharField(db_column='IdResponsable1', max_length=15, blank=True, null=True)  # Field name made lowercase.
     ocupacionresponsable1 = models.CharField(db_column='OcupacionResponsable1', max_length=50, blank=True, null=True)  # Field name made lowercase.
     nivelacademicoresponsable1 = models.IntegerField(db_column='NivelAcademicoResponsable1', blank=True, null=True)  # Field name made lowercase.
     parentesco1 = models.CharField(db_column='Parentesco1', max_length=50, blank=True, null=True)  # Field name made lowercase.
     nombrereposnsable2 = models.CharField(db_column='NombreReposnsable2', max_length=50, blank=True, null=True)  # Field name made lowercase.
     idresponsable2 = models.CharField(db_column='IdResponsable2', max_length=15, blank=True, null=True)  # Field name made lowercase.
     ocupacionresponsable2 = models.CharField(db_column='OcupacionResponsable2', max_length=50, blank=True, null=True)  # Field name made lowercase.
     nivelacademicoresponsable2 = models.IntegerField(db_column='NivelAcademicoResponsable2', blank=True, null=True)  # Field name made lowercase.
     parentesco2 = models.CharField(db_column='Parentesco2', max_length=50, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
#
     def __unicode__(self):
        return self.nombre_completo





class Personasporprocesoeducativo(models.Model):
     p_id = models.AutoField(db_column='P_Id', primary_key=True)  # Field name made lowercase.
     claveev = models.ForeignKey('ProcesoEducativo', models.DO_NOTHING, db_column='ClaveEV')  # Field name made lowercase.
     numero_identidad = models.CharField(db_column='Numero_identidad', max_length=15)  # Field name made lowercase.
     pxp_id = models.IntegerField(db_column='PxP_Id', blank=True, null=True)  # Field name made lowercase.
     ev_id = models.IntegerField(db_column='EV_Id', blank=True, null=True)  # Field name made lowercase.
     per_id = models.IntegerField(db_column='Per_Id', blank=True, null=True)  # Field name made lowercase.
     deserto = models.NullBooleanField(db_column='Deserto')  # Field name made lowercase.
     fechadesercion = models.CharField(db_column='FechaDesercion', max_length=10, blank=True, null=True)  # Field name made lowercase.
     causappaldesercion = models.IntegerField(db_column='CausaPpalDesercion', blank=True, null=True)  # Field name made lowercase.
     obscecap = models.TextField(db_column='ObsCECAP', blank=True, null=True)  # Field name made lowercase.
     fuesometidoacertificacion = models.NullBooleanField(db_column='FueSometidoACertificacion')  # Field name made lowercase.
     secertifico = models.NullBooleanField(db_column='SeCertifico')  # Field name made lowercase.
     tipocertificado = models.IntegerField(db_column='TipoCertificado', blank=True, null=True)  # Field name made lowercase.
     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
     edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
     egreso = models.CharField(db_column='egreso', blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
         return self.numero_identidad

     class Meta:
      #   managed = False
      #   db_table = 'PersonasPorProcesoEducativo'
         unique_together = (('claveev', 'numero_identidad'),)
#


#
class Catsexo(models.Model):
     id = models.DecimalField(db_column='Id', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
     sexo = models.CharField(db_column='Sexo', max_length=20, blank=True, null=True)  # Field name made lowercase.
     lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
     creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

     def __unicode__(self):
        return self.sexo



class Modulos(models.Model):
    claveev = models.ForeignKey('ProcesoEducativo', models.DO_NOTHING, db_column='ClaveEV')  # Field name made lowercase.
    m_dulo1 = models.CharField(db_column='Modulo1', max_length=100, blank=True,null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod1 = models.DateTimeField(db_column='Fechainiciomod1', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod1 = models.DateTimeField(db_column='Fechafinalmod1', blank=True,null=True)  # Field name made lowercase.
    horasteoricas1= models.CharField(db_column='horasteoricas1', max_length=100, blank=True,null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas1= models.CharField(db_column='horaspracticas1', max_length=100, blank=True,null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    instructormod1 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod1', blank=True,null=True, related_name='instructormod1')
    m_dulo2 = models.CharField(db_column='Modulo2', max_length=100, blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod2 = models.DateTimeField(db_column='Fechainiciomod2', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod2 = models.DateTimeField(db_column='Fechafinalmod2', blank=True,null=True)  # Field name made lowercase.
    horasteoricas2 = models.CharField(db_column='horasteoricas2', max_length=100, blank=True,null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas2 = models.CharField(db_column='horaspracticas2', max_length=100, blank=True,null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    instructormod2 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod2', blank=True,null=True, related_name='instructormod2')
    m_dulo3 = models.CharField(db_column='Modulo3', max_length=100, blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod3 = models.DateTimeField(db_column='Fechainiciomod3', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod3 = models.DateTimeField(db_column='Fechafinalmod3', blank=True,null=True)  # Field name made lowercase.
    horasteoricas3 = models.CharField(db_column='horasteoricas3', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas3 = models.CharField(db_column='horaspracticas3', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    instructormod3 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod3', blank=True,null=True, related_name='instructormod3')
    m_dulo4 = models.CharField(db_column='Modulo4', max_length=100, blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod4 = models.DateTimeField(db_column='Fechainiciomod4', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod4 = models.DateTimeField(db_column='Fechafinalmod4', blank=True,null=True)  # Field name made lowercase.
    horasteoricas4 = models.CharField(db_column='horasteoricas4', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas4 = models.CharField(db_column='horaspracticas4', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod4 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod4', blank=True,null=True, related_name='instructormod4')
    m_dulo5 = models.CharField(db_column='Modulo5', max_length=100, blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod5 = models.DateTimeField(db_column='Fechainiciomod5', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod5 = models.DateTimeField(db_column='Fechafinalmod5', blank=True,null=True)  # Field name made lowercase.
    horasteoricas5 = models.CharField(db_column='horasteoricas5', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas5 = models.CharField(db_column='horaspracticas5', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod5 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod5', blank=True,null=True, related_name='instructormod5')
    m_dulo6 = models.CharField(db_column='Modulo6', max_length=100, blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod6 = models.DateTimeField(db_column='Fechainiciomod6', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod6 = models.DateTimeField(db_column='Fechafinalmod6', blank=True,null=True)  # Field name made lowercase.
    horasteoricas6 = models.CharField(db_column='horasteoricas6', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas6 = models.CharField(db_column='horaspracticas6', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod6 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod6', blank=True,null=True, related_name='instructormod6')
    m_dulo7 = models.CharField(db_column='Modulo7', max_length=100, blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod7 = models.DateTimeField(db_column='Fechainiciomod7', blank=True,null=True)  # Field name made lowercase.
    fechafinalmod7 = models.DateTimeField(db_column='Fechafinalmod7', blank=True,null=True)  # Field name made lowercase.
    horasteoricas7 = models.CharField(db_column='horasteoricas7', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas7 = models.CharField(db_column='horaspracticas7', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod7 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod7', blank=True,
                                       null=True, related_name='instructormod7')
    m_dulo8 = models.CharField(db_column='Modulo8', max_length=100, blank=True,
                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod8 = models.DateTimeField(db_column='Fechainiciomod8', blank=True,
                                           null=True)  # Field name made lowercase.
    fechafinalmod8 = models.DateTimeField(db_column='Fechafinalmod8', blank=True,
                                          null=True)  # Field name made lowercase.
    horasteoricas8 = models.CharField(db_column='horasteoricas8', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas8 = models.CharField(db_column='horaspracticas8', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod8 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod8', blank=True,
                                       null=True, related_name='instructormod8')
    m_dulo9 = models.CharField(db_column='Modulo9', max_length=100, blank=True,
                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod9 = models.DateTimeField(db_column='Fechainiciomod9', blank=True,
                                           null=True)  # Field name made lowercase.
    fechafinalmod9 = models.DateTimeField(db_column='Fechafinalmod9', blank=True,
                                          null=True)  # Field name made lowercase.
    horasteoricas9 = models.CharField(db_column='horasteoricas9', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas9 = models.CharField(db_column='horaspracticas9', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod9 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod9', blank=True,
                                       null=True, related_name='instructormod9')
    m_dulo10 = models.CharField(db_column='Modulo10', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod10 = models.DateTimeField(db_column='Fechainiciomod10', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod10 = models.DateTimeField(db_column='Fechafinalmod10', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas10 = models.CharField(db_column='horasteoricas10', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas10 = models.CharField(db_column='horaspracticas10', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod10 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod10', blank=True,
                                        null=True, related_name='instructormod10')
    m_dulo11 = models.CharField(db_column='Modulo11', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod11 = models.DateTimeField(db_column='Fechainiciomod11', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod11 = models.DateTimeField(db_column='Fechafinalmod11', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas11 = models.CharField(db_column='horasteoricas11', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas11 = models.CharField(db_column='horaspracticas11', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod11 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod11', blank=True,
                                        null=True, related_name='instructormod11')
    m_dulo12 = models.CharField(db_column='Modulo12', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod12 = models.DateTimeField(db_column='Fechainiciomod12', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod12 = models.DateTimeField(db_column='Fechafinalmod12', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas12 = models.CharField(db_column='horasteoricas12', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas12 = models.CharField(db_column='horaspracticas12', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod12 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod12', blank=True,
                                        null=True, related_name='instructormod12')
    m_dulo13 = models.CharField(db_column='Modulo13', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod13 = models.DateTimeField(db_column='Fechainiciomod13', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod13 = models.DateTimeField(db_column='Fechafinalmod13', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas13 = models.CharField(db_column='horasteoricas13', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas13 = models.CharField(db_column='horaspracticas13', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod13 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod13', blank=True,
                                        null=True, related_name='instructormod13')
    m_dulo14 = models.CharField(db_column='Modulo14', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod14 = models.DateTimeField(db_column='Fechainiciomod14', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod14 = models.DateTimeField(db_column='Fechafinalmod14', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas14 = models.CharField(db_column='horasteoricas14', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas14 = models.CharField(db_column='horaspracticas14', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod14 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod14', blank=True,
                                        null=True, related_name='instructormod14')
    m_dulo15 = models.CharField(db_column='Modulo15', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod15 = models.DateTimeField(db_column='Fechainiciomod15', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod15 = models.DateTimeField(db_column='Fechafinalmod15', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas15 = models.CharField(db_column='horasteoricas15', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas15 = models.CharField(db_column='horaspracticas15', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod15 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod15', blank=True,
                                           null=True, related_name='instructormod15')
    m_dulo16 = models.CharField(db_column='Modulo16', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod16 = models.DateTimeField(db_column='Fechainiciomod16', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod16 = models.DateTimeField(db_column='Fechafinalmod16', blank=True,
                                           null=True)  # Field name made lowercase.
    instructormod16 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod16', blank=True,
                                        null=True, related_name='instructormod16')
    m_dulo17 = models.CharField(db_column='Modulo17', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod17 = models.DateTimeField(db_column='Fechainiciomod17', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod17 = models.DateTimeField(db_column='Fechafinalmod17', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas17 = models.CharField(db_column='horasteoricas17', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas17 = models.CharField(db_column='horaspracticas17', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod17 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod17', blank=True,
                                        null=True, related_name='instructormod17')
    m_dulo18 = models.CharField(db_column='Modulo18', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod18 = models.DateTimeField(db_column='Fechainiciomod18', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod18 = models.DateTimeField(db_column='Fechafinalmod18', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas18 = models.CharField(db_column='horasteoricas18', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas18 = models.CharField(db_column='horaspracticas18', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod18 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod18', blank=True,
                                        null=True, related_name='instructormod18')
    m_dulo19 = models.CharField(db_column='Modulo19', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod19 = models.DateTimeField(db_column='Fechainiciomod19', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod19 = models.DateTimeField(db_column='Fechafinalmod19', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas19 = models.CharField(db_column='horasteoricas19', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas19 = models.CharField(db_column='horaspracticas19', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    instructormod19 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod19', blank=True,
                                        null=True, related_name='instructormod19')
    m_dulo20 = models.CharField(db_column='Modulo20', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod20 = models.DateTimeField(db_column='Fechainiciomod20', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod20 = models.DateTimeField(db_column='Fechafinalmod20', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas20 = models.CharField(db_column='horasteoricas20', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas20 = models.CharField(db_column='horaspracticas20', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod20 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod20', blank=True,
                                        null=True, related_name='instructormod20')
    m_dulo21 = models.CharField(db_column='Modulo21', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod21 = models.DateTimeField(db_column='Fechainiciomod21', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod21 = models.DateTimeField(db_column='Fechafinalmod21', blank=True,
                                           null=True)  # Field name made lowercase.

    horasteoricas21 = models.CharField(db_column='horasteoricas21', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas21 = models.CharField(db_column='horaspracticas21', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod21 = models.ForeignKey(Cateducadores, db_column='instructormod21', blank=True, null=True,
                                        related_name='instructormod21')
    m_dulo22 = models.CharField(db_column='Modulo22', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod22 = models.DateTimeField(db_column='Fechainiciomod22', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod22 = models.DateTimeField(db_column='Fechafinalmod22', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas22 = models.CharField(db_column='horasteoricas22', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas22 = models.CharField(db_column='horaspracticas22', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod22 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod22', blank=True,
                                        null=True, related_name='instructormod22')
    m_dulo23 = models.CharField(db_column='Modulo23', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod23 = models.DateTimeField(db_column='Fechainiciomod23', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod23 = models.DateTimeField(db_column='Fechafinalmod23', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas23 = models.CharField(db_column='horasteoricas23', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas23 = models.CharField(db_column='horaspracticas23', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod23 = models.ForeignKey(Cateducadores, db_column='instructormod23', blank=True, null=True,
                                        related_name='instructormod23')
    m_dulo24 = models.CharField(db_column='Modulo24', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod24 = models.DateTimeField(db_column='Fechainiciomod24', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod24 = models.DateTimeField(db_column='Fechafinalmod24', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas24 = models.CharField(db_column='horasteoricas24', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas24 = models.CharField(db_column='horaspracticas24', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod24 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod24', blank=True,
                                        null=True, related_name='instructormod24')
    m_dulo25 = models.CharField(db_column='Modulo25', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod25 = models.DateTimeField(db_column='Fechainiciomod25', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod25 = models.DateTimeField(db_column='Fechafinalmod25', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas25 = models.CharField(db_column='horasteoricas25', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas25 = models.CharField(db_column='horaspracticas25', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod25 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod25', blank=True,
                                        null=True, related_name='instructormod25')
    m_dulo26 = models.CharField(db_column='Modulo26', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod26 = models.DateTimeField(db_column='Fechainiciomod26', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod26 = models.DateTimeField(db_column='Fechafinalmod26', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas26 = models.CharField(db_column='horasteoricas26', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas26 = models.CharField(db_column='horaspracticas26', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod26 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod26', blank=True,
                                        null=True, related_name='instructormod26')
    m_dulo27 = models.CharField(db_column='Modulo27', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod27 = models.DateTimeField(db_column='Fechainiciomod27', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod27 = models.DateTimeField(db_column='Fechafinalmod27', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas27 = models.CharField(db_column='horasteoricas27', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas27 = models.CharField(db_column='horaspracticas27', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod27 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod27', blank=True,
                                        null=True, related_name='instructormod27')
    m_dulo28 = models.CharField(db_column='Modulo28', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod28 = models.DateTimeField(db_column='Fechainiciomod28', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod28 = models.DateTimeField(db_column='Fechafinalmod28', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas28 = models.CharField(db_column='horasteoricas28', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas28 = models.CharField(db_column='horaspracticas28', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    instructormod28 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod28', blank=True,
                                        null=True, related_name='instructormod28')
    m_dulo29 = models.CharField(db_column='Modulo29', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod29 = models.DateTimeField(db_column='Fechainiciomod29', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod29 = models.DateTimeField(db_column='Fechafinalmod29', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas29 = models.CharField(db_column='horasteoricas29', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas29 = models.CharField(db_column='horaspracticas29', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod29 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod29', blank=True,
                                        null=True, related_name='instructormod29')

    m_dulo30 = models.CharField(db_column='MOdulo30', max_length=100, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechainiciomod30 = models.DateTimeField(db_column='Fechainiciomod30', blank=True,
                                            null=True)  # Field name made lowercase.
    fechafinalmod30 = models.DateTimeField(db_column='Fechafinalmod30', blank=True,
                                           null=True)  # Field name made lowercase.
    horasteoricas30 = models.CharField(db_column='horasteoricas30', max_length=100, blank=True,
                                      null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.
    horaspracticas30 = models.CharField(db_column='horaspracticas30', max_length=100, blank=True,
                                       null=True)  # Field  lowercase. Field renamed to remove unsuitable characters.

    instructormod30 = models.ForeignKey(Cateducadores, models.DO_NOTHING, db_column='instructormod30', blank=True,
                                        null=True, related_name='instructormod30')




class Evaluaciones(models.Model):
            clave = models.ForeignKey('Modulos', models.DO_NOTHING, db_column='Clave')  # Field name made lowercase.
            claveev = models.ForeignKey('ProcesoEducativo', models.DO_NOTHING, db_column='ClaveEV')  # Field name made lowercase.
            numero_identidad = models.CharField(db_column='Numero_identidad', max_length=15)  # Field name made lowercase.
            per_id = models.IntegerField(db_column='PER_Id', blank=True, null=True)  # Field name made lowercase.
            ev_id = models.IntegerField(db_column='Ev_Id', blank=True, null=True)  # Field name made lowercase.
            cd_id = models.IntegerField(db_column='CD_Id', blank=True, null=True)  # Field name made lowercase.
            horasteoria1 = models.FloatField(db_column='HorasTeoria1', blank=True, null=True)  # Field name made lowercase.
            horaspractica1 = models.FloatField(db_column='HorasPractica1', blank=True, null=True)  # Field name made lowercase.
            notateorica1 = models.FloatField(db_column='NotaTeorica1', blank=True, null=True)  # Field name made lowercase.
            notapractica1 = models.FloatField(db_column='NotaPractica1', blank=True, null=True)  # Field name made lowercase.
            horasteoria2 = models.FloatField(db_column='HorasTeoria2', blank=True, null=True)  # Field name made lowercase.
            horaspractica2 = models.FloatField(db_column='HorasPractica2', blank=True, null=True)  # Field name made lowercase.
            notateorica2 = models.FloatField(db_column='NotaTeorica2', blank=True, null=True)  # Field name made lowercase.
            notapractica2 = models.FloatField(db_column='NotaPractica2', blank=True, null=True)  # Field name made lowercase.
            horasteoria3 = models.FloatField(db_column='HorasTeoria3', blank=True, null=True)  # Field name made lowercase.
            horaspractica3 = models.FloatField(db_column='HorasPractica3', blank=True, null=True)  # Field name made lowercase.
            notateorica3 = models.FloatField(db_column='NotaTeorica3', blank=True, null=True)  # Field name made lowercase.
            notapractica3 = models.FloatField(db_column='NotaPractica3', blank=True, null=True)  # Field name made lowercase.
            horasteoria4 = models.FloatField(db_column='HorasTeoria4', blank=True, null=True)  # Field name made lowercase.
            horaspractica4 = models.FloatField(db_column='HorasPractica4', blank=True, null=True)  # Field name made lowercase.
            notateorica4 = models.FloatField(db_column='NotaTeorica4', blank=True, null=True)  # Field name made lowercase.
            notapractica4 = models.FloatField(db_column='NotaPractica4', blank=True, null=True)  # Field name made lowercase.
            horasteoria5 = models.FloatField(db_column='HorasTeoria5', blank=True, null=True)  # Field name made lowercase.
            horaspractica5 = models.FloatField(db_column='HorasPractica5', blank=True, null=True)  # Field name made lowercase.
            notateorica5 = models.FloatField(db_column='NotaTeorica5', blank=True, null=True)  # Field name made lowercase.
            notapractica5 = models.FloatField(db_column='NotaPractica5', blank=True, null=True)  # Field name made lowercase.
            horasteoria6 = models.FloatField(db_column='HorasTeoria6', blank=True, null=True)  # Field name made lowercase.
            horaspractica6 = models.FloatField(db_column='HorasPractica6', blank=True, null=True)  # Field name made lowercase.
            notateorica6 = models.FloatField(db_column='NotaTeorica6', blank=True, null=True)  # Field name made lowercase.
            notapractica6 = models.FloatField(db_column='NotaPractica6', blank=True, null=True)  # Field name made lowercase.
            horasteoria7 = models.FloatField(db_column='HorasTeoria7', blank=True, null=True)  # Field name made lowercase.
            horaspractica7 = models.FloatField(db_column='HorasPractica7', blank=True, null=True)  # Field name made lowercase.
            notateorica7 = models.FloatField(db_column='NotaTeorica7', blank=True, null=True)  # Field name made lowercase.
            notapractica7 = models.FloatField(db_column='NotaPractica7', blank=True, null=True)  # Field name made lowercase.
            horasteoria8 = models.FloatField(db_column='HorasTeoria8', blank=True, null=True)  # Field name made lowercase.
            horaspractica8 = models.FloatField(db_column='HorasPractica8', blank=True, null=True)  # Field name made lowercase.
            notateorica8 = models.FloatField(db_column='NotaTeorica8', blank=True, null=True)  # Field name made lowercase.
            notapractica8 = models.FloatField(db_column='NotaPractica8', blank=True, null=True)  # Field name made lowercase.
            horasteoria9 = models.FloatField(db_column='HorasTeoria9', blank=True, null=True)  # Field name made lowercase.
            horaspractica9 = models.FloatField(db_column='HorasPractica9', blank=True, null=True)  # Field name made lowercase.
            notateorica9 = models.FloatField(db_column='NotaTeorica9', blank=True, null=True)  # Field name made lowercase.
            notapractica9 = models.FloatField(db_column='NotaPractica9', blank=True, null=True)  # Field name made lowercase.
            horasteoria10 = models.FloatField(db_column='HorasTeoria10', blank=True, null=True)  # Field name made lowercase.
            horaspractica10 = models.FloatField(db_column='HorasPractica10', blank=True, null=True)  # Field name made lowercase.
            notateorica10 = models.FloatField(db_column='NotaTeorica10', blank=True, null=True)  # Field name made lowercase.
            notapractica10 = models.FloatField(db_column='NotaPractica10', blank=True, null=True)  # Field name made lowercase.
            horasteoria11 = models.FloatField(db_column='HorasTeoria11', blank=True, null=True)  # Field name made lowercase.
            horaspractica11 = models.FloatField(db_column='HorasPractica11', blank=True, null=True)  # Field name made lowercase.
            notateorica11 = models.FloatField(db_column='NotaTeorica11', blank=True, null=True)  # Field name made lowercase.
            notapractica11 = models.FloatField(db_column='NotaPractica11', blank=True, null=True)  # Field name made lowercase.
            horasteoria12 = models.FloatField(db_column='HorasTeoria12', blank=True, null=True)  # Field name made lowercase.
            horaspractica12 = models.FloatField(db_column='HorasPractica12', blank=True, null=True)  # Field name made lowercase.
            notateorica12 = models.FloatField(db_column='NotaTeorica12', blank=True, null=True)  # Field name made lowercase.
            notapractica12 = models.FloatField(db_column='NotaPractica12', blank=True, null=True)  # Field name made lowercase.
            horasteoria13 = models.FloatField(db_column='HorasTeoria13', blank=True, null=True)  # Field name made lowercase.
            horaspractica13 = models.FloatField(db_column='HorasPractica13', blank=True, null=True)  # Field name made lowercase.
            notateorica13 = models.FloatField(db_column='NotaTeorica13', blank=True, null=True)  # Field name made lowercase.
            notapractica13 = models.FloatField(db_column='NotaPractica13', blank=True, null=True)  # Field name made lowercase.
            horasteoria14 = models.FloatField(db_column='HorasTeoria14', blank=True, null=True)  # Field name made lowercase.
            horaspractica14 = models.FloatField(db_column='HorasPractica14', blank=True, null=True)  # Field name made lowercase.
            notateorica14 = models.FloatField(db_column='NotaTeorica14', blank=True, null=True)  # Field name made lowercase.
            notapractica14 = models.FloatField(db_column='NotaPractica14', blank=True, null=True)  # Field name made lowercase.
            horasteoria15 = models.FloatField(db_column='HorasTeoria15', blank=True, null=True)  # Field name made lowercase.
            horaspractica15 = models.FloatField(db_column='HorasPractica15', blank=True, null=True)  # Field name made lowercase.
            notateorica15 = models.FloatField(db_column='NotaTeorica15', blank=True, null=True)  # Field name made lowercase.
            notapractica15 = models.FloatField(db_column='NotaPractica15', blank=True, null=True)  # Field name made lowercase.
            horasteoria16 = models.FloatField(db_column='HorasTeoria16', blank=True, null=True)  # Field name made lowercase.
            horaspractica16 = models.FloatField(db_column='HorasPractica16', blank=True, null=True)  # Field name made lowercase.
            notateorica16 = models.FloatField(db_column='NotaTeorica16', blank=True, null=True)  # Field name made lowercase.
            notapractica16 = models.FloatField(db_column='NotaPractica16', blank=True, null=True)  # Field name made lowercase.
            horasteoria17 = models.FloatField(db_column='HorasTeoria17', blank=True, null=True)  # Field name made lowercase.
            horaspractica17 = models.FloatField(db_column='HorasPractica17', blank=True, null=True)  # Field name made lowercase.
            notateorica17 = models.FloatField(db_column='NotaTeorica17', blank=True, null=True)  # Field name made lowercase.
            notapractica17 = models.FloatField(db_column='NotaPractica17', blank=True, null=True)  # Field name made lowercase.
            horasteoria18 = models.FloatField(db_column='HorasTeoria18', blank=True, null=True)  # Field name made lowercase.
            horaspractica18 = models.FloatField(db_column='HorasPractica18', blank=True, null=True)  # Field name made lowercase.
            notateorica18 = models.FloatField(db_column='NotaTeorica18', blank=True, null=True)  # Field name made lowercase.
            notapractica18 = models.FloatField(db_column='NotaPractica18', blank=True, null=True)  # Field name made lowercase.
            horasteoria19 = models.FloatField(db_column='HorasTeoria19', blank=True, null=True)  # Field name made lowercase.
            horaspractica19 = models.FloatField(db_column='HorasPractica19', blank=True, null=True)  # Field name made lowercase.
            notateorica19 = models.FloatField(db_column='NotaTeorica19', blank=True, null=True)  # Field name made lowercase.
            notapractica19 = models.FloatField(db_column='NotaPractica19', blank=True, null=True)  # Field name made lowercase.
            horasteoria20 = models.FloatField(db_column='HorasTeoria20', blank=True, null=True)  # Field name made lowercase.
            horaspractica20 = models.FloatField(db_column='HorasPractica20', blank=True, null=True)  # Field name made lowercase.
            notateorica20 = models.FloatField(db_column='NotaTeorica20', blank=True, null=True)  # Field name made lowercase.
            notapractica20 = models.FloatField(db_column='NotaPractica20', blank=True, null=True)  # Field name made lowercase.
            observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
            pasanopasa = models.NullBooleanField(db_column='PasaNoPasa')  # Field name made lowercase.
            lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
            creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
            horasteoria21 = models.FloatField(db_column='HorasTeoria21', blank=True, null=True)  # Field name made lowercase.
            horaspractica21 = models.FloatField(db_column='HorasPractica21', blank=True, null=True)  # Field name made lowercase.
            notateorica21 = models.FloatField(db_column='NotaTeorica21', blank=True, null=True)  # Field name made lowercase.
            notapractica21 = models.FloatField(db_column='NotaPractica21', blank=True, null=True)  # Field name made lowercase.
            horasteoria22 = models.FloatField(db_column='HorasTeoria22', blank=True, null=True)  # Field name made lowercase.
            horaspractica22 = models.FloatField(db_column='HorasPractica22', blank=True, null=True)  # Field name made lowercase.
            notateorica22 = models.FloatField(db_column='NotaTeorica22', blank=True, null=True)  # Field name made lowercase.
            notapractica22 = models.FloatField(db_column='NotaPractica22', blank=True, null=True)  # Field name made lowercase.
            horasteoria23 = models.FloatField(db_column='HorasTeoria23', blank=True, null=True)  # Field name made lowercase.
            horaspractica23 = models.FloatField(db_column='HorasPractica23', blank=True, null=True)  # Field name made lowercase.
            notateorica23 = models.FloatField(db_column='NotaTeorica23', blank=True, null=True)  # Field name made lowercase.
            notapractica23 = models.FloatField(db_column='NotaPractica23', blank=True, null=True)  # Field name made lowercase.
            horasteoria24 = models.FloatField(db_column='HorasTeoria24', blank=True, null=True)  # Field name made lowercase.
            horaspractica24 = models.FloatField(db_column='HorasPractica24', blank=True, null=True)  # Field name made lowercase.
            notateorica24 = models.FloatField(db_column='NotaTeorica24', blank=True, null=True)  # Field name made lowercase.
            notapractica24 = models.FloatField(db_column='NotaPractica24', blank=True, null=True)  # Field name made lowercase.
            horasteoria25 = models.FloatField(db_column='HorasTeoria25', blank=True, null=True)  # Field name made lowercase.
            horaspractica25 = models.FloatField(db_column='HorasPractica25', blank=True, null=True)  # Field name made lowercase.
            notateorica25 = models.FloatField(db_column='NotaTeorica25', blank=True, null=True)  # Field name made lowercase.
            notapractica25 = models.FloatField(db_column='NotaPractica25', blank=True, null=True)  # Field name made lowercase.
            horasteoria26 = models.FloatField(db_column='HorasTeoria26', blank=True, null=True)  # Field name made lowercase.
            horaspractica26 = models.FloatField(db_column='HorasPractica26', blank=True, null=True)  # Field name made lowercase.
            notateorica26 = models.FloatField(db_column='NotaTeorica26', blank=True, null=True)  # Field name made lowercase.
            notapractica26 = models.FloatField(db_column='NotaPractica26', blank=True, null=True)  # Field name made lowercase.
            horasteoria27 = models.FloatField(db_column='HorasTeoria27', blank=True, null=True)  # Field name made lowercase.
            horaspractica27 = models.FloatField(db_column='HorasPractica27', blank=True, null=True)  # Field name made lowercase.
            notateorica27 = models.FloatField(db_column='NotaTeorica27', blank=True, null=True)  # Field name made lowercase.
            notapractica27 = models.FloatField(db_column='NotaPractica27', blank=True, null=True)  # Field name made lowercase.
            horasteoria28 = models.FloatField(db_column='HorasTeoria28', blank=True, null=True)  # Field name made lowercase.
            horaspractica28 = models.FloatField(db_column='HorasPractica28', blank=True, null=True)  # Field name made lowercase.
            notateorica28 = models.FloatField(db_column='NotaTeorica28', blank=True, null=True)  # Field name made lowercase.
            notapractica28 = models.FloatField(db_column='NotaPractica28', blank=True, null=True)  # Field name made lowercase.
            horasteoria29 = models.FloatField(db_column='HorasTeoria29', blank=True, null=True)  # Field name made lowercase.
            horaspractica29 = models.FloatField(db_column='HorasPractica29', blank=True, null=True)  # Field name made lowercase.
            notateorica29 = models.FloatField(db_column='NotaTeorica29',blank=True,null=True)

            #class Meta:
             #   managed = False
             #   db_table = 'Evaluaciones'


            def __unicode__(self):
                 return self.numero_identidad

            unique_together = (('claveev', 'numero_identidad'),)



