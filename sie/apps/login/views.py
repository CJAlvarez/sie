# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
import json
from pyodbc import IntegrityError

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
import numpy as np
from django.db import connection
from django.http import Http404
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from update import update
import csv

#from conexion import connection
from forms import *
from ...apps.login.models import *

# ##################USUARIOS############################
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from sie.apps.login.models import Perfil
from datetime import date, datetime
from dateutil import parser
from django.contrib import messages


def vista_index(request):
    users=Perfil.objects.all()
    return render_to_response("login.html",{'users':users})

def vista_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/dashboard/")
    else:
        men="Usuario o Contraseña Invalido "
        return render_to_response('login.html', {'men': men})
@login_required
def vista_dashboard(request):
    user = request.user
    return render_to_response("dashboard.html", {'user': user})
@login_required
def vista_logout(request):
    logout(request)
    return redirect('/')
    # ######################################################
    #
 ############Proceso Educativo############################3


##############################PROCESO EDUCATIVO##################################################################
@login_required
def vista_proceso_educativo(request):
         user = request.user
         ce= user.clavecap
         cuenta = ProcesoEducativo.objects.filter(clavececap__contains=ce).count()
         user = request.user
         if request.POST:
             form = ProcesoForm(request.POST, request.FILES)
             print form
             if form.is_valid():
                 form.save()
                # messages.success(request, 'Profile details updated.')
                 return HttpResponseRedirect("/proceso_educativo/")
         else:
             form = ProcesoForm()
         args = {}
         args.update(csrf(request))
         args['form'] = form
         us=user.username
         lista=ProcesoEducativo.objects.filter(clavececap=ce)
         paginator = Paginator(lista,10000)  # Show 25 contacts per page
         page = request.GET.get('page')
         try:
             contacts = paginator.page(page)
         except PageNotAnInteger:
             contacts = paginator.page(1)
         except EmptyPage:
             contacts = paginator.page(paginator.num_pages)
         departamentos=Catdepartamentos.objects.all()
         educativa=Catopcioneseducativas.objects.all()
         material=Catmaterialdidactico.objects.all()
         modalidades=Catmodalidades.objects.all()
         tmodalidades=Cattipomodalidad.objects.all()
         proyectos=Proyectos.objects.all()
         sectores=Catsectoreseconomicos.objects.all()
         educadores=Cateducadores.objects.all()
         a=np.random.randint(1, 9999999)
         sede=Cattipossedes.objects.all()
         return render_to_response('proceso_educativo.html', {"contacts":contacts,"educadores":educadores,"sede":sede,"sectores":sectores,"proyectos":proyectos,"tmodalidades":tmodalidades,"modalidades":modalidades,"material":material,"educativa":educativa,"departamentos":departamentos,"form": form,"lista":lista,"ce":ce,"us":us,"a":a,"user":user,"cuenta":cuenta})


@login_required
def vista_borrar_proceso(request,id_borrarproceso):
    try:   
       borrar = ProcesoEducativo.objects.get(cecap_id=id_borrarproceso)
       borrar.delete()
    except IntegrityError:
      return HttpResponse('<script text/javascript>alert(\'Advertencia:No se puede borrar tiene evaluaciones.\'); window.location="/proceso_educativo/"</script>')
       #messages.success(request,"Usuario Borrado!!")
    return HttpResponseRedirect("/proceso_educativo/")












@login_required
def vista_editar_proceso(request,id_editarproceso):
    editar = ProcesoEducativo.objects.get(cecap_id=id_editarproceso)
    if request.method == "POST":
        formulario = ProcesoForm(request.POST, instance=editar)
        print formulario
        if formulario.is_valid():
            formulario.save()
            return HttpResponse('<script text/javascript>alert(\'Actualización Realizada\'); window.location="/proceso_educativo/"</script>')
            #  messages.success(request,"Usuario Actualizado!!!")
    else:
        formulario = ProcesoForm(instance=editar)
    return render_to_response('editar_proceso_educativa.html', {"formulario": formulario})
#################################################################################################################

##############################GESTION PARTICIPANTES############################################################

@login_required
def vista_participantes(request):
         user = request.user
         print user
         if request.POST:
             form = ParticipantesForm(request.POST, request.FILES)
             print form
             if form.is_valid():
                 form.save()
                 print form
                #messages.success(request, 'Profile details updated.')
                 return HttpResponseRedirect("/personas/")
         else:
             form = ParticipantesForm()
         args = {}
         args.update(csrf(request))
         args['form'] = form
         cuenta = Personas.objects.all().count()

         user = request.user
         ce= user.clavecap
         us=user.username
         niveleducativo=Catniveleducativo.objects.all()
         estado=Catestadocivil.objects.all()
         #lista=Personas.objects.filter(clavececap=ce)
         lista=Personas.objects.all()
         conte=Personas.objects.all().count()
         print conte
         paginator = Paginator(lista, 10000)  # Show 25 contsacts per page

         page = request.GET.get('page')
         try:
             contacts = paginator.page(page)
         except PageNotAnInteger:
             # If page is not an integer, deliver first page.
             contacts = paginator.page(1)
         except EmptyPage:
             # If page is out of range (e.g. 9999), deliver last page of results.
             contacts = paginator.page(paginator.num_pages)
         nacionalidad=Catnacionalidad.objects.all()     
         departamentos=Catdepartamentos.objects.all()
         educativa=Catopcioneseducativas.objects.all()
         material=Catmaterialdidactico.objects.all()
         modalidades=Catmodalidades.objects.all()
         tmodalidades=Cattipomodalidad.objects.all()
         proyectos=Proyectos.objects.all()
         sectores=Catsectoreseconomicos.objects.all()
         etnia=Catetnias.objects.all()
         a=np.random.randint(1, 9999999)
         grado=Catgradoalcanzado.objects.all()
         estudiando=Catestudia.objects.all()
         discapacidad=Catdiscapacidades.objects.all()   
         return render_to_response('personas.html', {"nacionalidad":nacionalidad,"discapacidad":discapacidad,"estudiando":estudiando,"grado":grado,"conte":conte,"contacts":contacts,"cuenta":cuenta,"etnia":etnia,"niveleducativo":niveleducativo,"estado":estado,"sectores":sectores,"proyectos":proyectos,"tmodalidades":tmodalidades,"modalidades":modalidades,"material":material,"educativa":educativa,"departamentos":departamentos,"form": form,"lista":lista,"ce":ce,"us":us,"a":a,"user":user})
@login_required
def vista_borrar_participantes(request,id_borrarparticipante):
       borrar = Personas.objects.get(pk=id_borrarparticipante)
       borrar.delete()
       #messages.success(request,"Usuario Borrado!!")
       return HttpResponseRedirect("/personas/")
@login_required
def vista_editar_participantes(request,id_editarparticipantes):
    editar = Personas.objects.get(pk=id_editarparticipantes)
    if request.method == "POST":
        formulario = ParticipantesForm(request.POST, instance=editar)
        print formulario
        if formulario.is_valid():
            formulario.save()
            return HttpResponse('<script text/javascript>alert(\'Actualización Realizada\'); window.location="/personas/"</script>')

            #return HttpResponseRedirect("/personas/")
            #  messages.success(request,"Usuario Actualizado!!!")
    else:
        formulario = ParticipantesForm(instance=editar)
    return render_to_response('editar_personas.html', {"formulario": formulario})
@login_required
def vista_busquedadidentidad(request):
        if request.is_ajax():
            id= request.POST['identidad']
            identidad= Personas.objects.filter(numero_identidad=id)
            data = [{'numero_identidad': row.numero_identidad,'nombre_completo':row.nombre_completo} for row in identidad]
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            messages = "No es ajax"
            return HttpResponse(messages)

def calcular_edad(request):
    if request.is_ajax():
        fecha_n = request.POST['fecha']
        time=parser.parse(fecha_n)
        fecha_nac = (time)
        diferencia_fechas = datetime.today()-fecha_nac
        diferencia_fechas_dias = diferencia_fechas.days
        edad_numerica = diferencia_fechas_dias * 0.00273973
        edad_meses=(diferencia_fechas.days)*0.0328767
        print edad_numerica
        print edad_meses
        data = [{'edad_numerica': edad_numerica,'edad_meses':edad_meses}]
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        messages = "No es ajax"
        return HttpResponse(messages)
####################################################################################################################

#########Matricula participantes########################
#@login_required
#def vista_matricula_ajax(request):
  #  if request.method == "POST":
   #     try:
    #        c = request.POST['clave']
     #       i = request.POST.getlist('videntidad')
      #      print c 
      #      print i 
      #  except MultiValueDictKeyError:
      #      return HttpResponse('<script text/javascript>alert(\'Ingrese un Valor Valido\'); window.location="/matricula/"</script>')
      #  cursor = connection.cursor()
      #  try:
      #      for t in i:
      #          lista = ''.join(t)
      #          cursor.execute("INSERT INTO login_personasporprocesoeducativo (claveev,Numero_identidad)VALUES('%s','%s');" % (c,lista))
      #          cursor.execute("INSERT INTO login_evaluaciones (Numero_identidad, claveEV,clave)VALUES('%s','%s','1');"%(lista,c))
      #  except IntegrityError:
      #   return HttpResponse('<script text/javascript>alert(\'Ya Esta Registrado\'); window.location="/matricula/"</script>')
    #return HttpResponse('<script text/javascript>alert(\'Exitosamente Matriculado\'); window.location="/matricula/"</script>')
@login_required
@login_required
def vista_matricula_ajax(request):
    if request.method == "POST":
        try:
            c = request.POST['clave']
            i = request.POST.getlist('videntidad')
            modulos = Modulos.objects.filter(claveev=c).values_list('pk', flat=True)
            if modulos:
                cursor = connection.cursor()
                for a in modulos:
                    try:
                        for t in i:
                            lista = ''.join(t)
                            cursor.execute(
                                "INSERT INTO login_personasporprocesoeducativo (claveev,numero_identidad) VALUES('%s','%s');" % (
                                    c, lista))
                            cursor.execute(
                                "INSERT INTO login_evaluaciones (numero_identidad,claveev,clave)VALUES('%s','%s','%s');" % (
                                    lista, c, a))
                    except IntegrityError:
                        return HttpResponse(
                            '<script text/javascript>alert(\'Mensaje:Se encuentra registrado\'); window.location="/matricula/"</script>')
            else:
                return HttpResponse(
                    '<script text/javascript>alert(\'Advertencia:No se matriculo porque no tiene un modulo asignado este proceso\'); window.location="/matricula/"</script>')


        except MultiValueDictKeyError:
            return HttpResponse(
                '<script text/javascript>alert(\'Ingrese un Valor Valido\'); window.location="/matricula/"</script>')

    return HttpResponse(
        '<script text/javascript>alert(\'Mensaje:Exitosamente Matriculado(a)\'); window.location="/matricula/"</script>')




@login_required
def vista_matricula(request):
    user = request.user
    ce = user.clavecap
    personas=Personas.objects.all()
    lista = ProcesoEducativo.objects.filter(clavececap=ce)
    cursor = connection.cursor()
    cursor.execute("select procesoeducativo.cd_nombre,personas.nombre_completo,personas.numero_identidad,catdepartamentos.dep_departamento,catmunicipios.mun_municipio,cataldeas.nombrealdea,catcaserios.nombrecaserio,p_id from login_personas as personas inner join  login_personasporprocesoeducativo as personasporprocesoeducativo on personas.numero_identidad=personasporprocesoeducativo.numero_identidad inner join login_procesoeducativo as procesoeducativo on procesoeducativo.clave=personasporprocesoeducativo.claveev inner join login_catdepartamentos as  catdepartamentos on catdepartamentos.dep_id=personas.dep_id inner join login_catmunicipios  as catmunicipios  on catmunicipios.dep_id=catdepartamentos.dep_id and personas.mun_id=catmunicipios.mun_id   inner join login_cataldeas  as cataldeas  on cataldeas.idmunicipio=catmunicipios.mun_id and personas.al_id=cataldeas.idaldea and cataldeas.idmunicipio=catmunicipios.mun_id inner join login_catcaserios as catcaserios  on catcaserios.idcaserio=personas.ca_id and catcaserios.idaldea=cataldeas.idaldea")
    entries = [dict(title=row[0], text=row[1],identidad=row[2],dep=row[3],mun=row[4],al=row[5],ca=row[6],id=row[7]) for row in cursor.fetchall()]
    contexto={'personas': personas,'ce':ce,'user':user,'lista':lista,'row':entries,}
    return render(request,"matricula.html",contexto)

@login_required
def vista_borrar_matriculado(request,id_borrarmatriculado,identidad,clave):
    borrar = Personasporprocesoeducativo.objects.get(p_id=id_borrarmatriculado)
    borrar.delete()
    user = request.user
    ce = user.clavecap
    lista = ProcesoEducativo.objects.filter(clavececap=ce).values("clave")
    borrarnota=Evaluaciones.objects.filter(claveev=clave,numero_identidad=identidad).delete()
    return HttpResponseRedirect("/matricula/")


    
@login_required
def vista_busquedappp(request):
    if request.is_ajax():
        b = request.POST['id']
        cursor = connection.cursor()
        #cursor.execute("select ProcesoEducativo.CD_Nombre,Personas.Nombre_Completo,Personas.Numero_identidad,CatDepartamentos.Dep_Departamento,CatMunicipios.Mun_Municipio,CatAldeas.NombreAldea,CatCaserios.NombreCaserio,P_id,Claveev from login_Personas as Personas inner join  login_PersonasPorProcesoEducativo as PersonasPorProcesoEducativo on Personas.Numero_identidad=PersonasPorProcesoEducativo.Numero_identidad inner join login_ProcesoEducativo as ProcesoEducativo on ProcesoEducativo.Clave=PersonasPorProcesoEducativo.ClaveEV inner join login_CatDepartamentos as  CatDepartamentos on CatDepartamentos.Dep_Id=Personas.Dep_Id inner join login_CatMunicipios  as CatMunicipios  on CatMunicipios.Dep_Id=CatDepartamentos.Dep_Id and personas.Mun_id=CatMunicipios.Mun_Id  inner join login_CatAldeas  as CatAldeas  on CatAldeas.IdMunicipio=CatMunicipios.Mun_Id and Personas.Aldea=CatAldeas.IdAldea and CatAldeas.IdMunicipio=CatMunicipios.Mun_Id inner join login_CatCaserios as CatCaserios  on CatCaserios.IdCaserio=Personas.Caserio and CatCaserios.IdAldea=CatAldeas.IdAldea WHERE ClaveEV LIKE ('%s');" % (b))
        cursor.execute("select procesoeducativo.cd_nombre,personas.nombre_completo,personas.numero_identidad,catdepartamentos.dep_departamento,catmunicipios.mun_municipio,cataldeas.nombrealdea,catcaserios.nombrecaserio,p_id,claveev from login_personas as personas inner join  login_personasporprocesoeducativo as personasporprocesoeducativo on personas.numero_identidad=personasporprocesoeducativo.numero_identidad inner join login_procesoeducativo as procesoeducativo on procesoeducativo.clave=personasporprocesoeducativo.claveev inner join login_catdepartamentos as  catdepartamentos on catdepartamentos.dep_id=personas.dep_id inner join login_catmunicipios  as catmunicipios  on catmunicipios.dep_id=catdepartamentos.dep_id and personas.mun_id=catmunicipios.mun_id  inner join login_cataldeas  as cataldeas  on cataldeas.idmunicipio=catmunicipios.mun_id and personas.al_id=cataldeas.idaldea and cataldeas.idmunicipio=catmunicipios.mun_id inner join login_catcaserios as catcaserios  on catcaserios.idcaserio=personas.ca_id and catcaserios.idaldea=cataldeas.idaldea WHERE claveev LIKE ('%s');" % (b))
        busqueda=cursor.fetchall()
    #data = [dict(title=row[0], text=row[1],identidad=row[2],dep=row[3],mun=row[4],al=row[5],ca=row[6],id=row[7]) for row in cursor.fetchall()]
        data = [{'proceso': row[0],'nombre': row[1],'ide': row[2],'dep': row[3],'mun': row[4],'al': row[5],'ca': row[6],'id': row[7],'claveev': row[8]} for row in busqueda]
        print type(data)
    #print data
        return HttpResponse(json.dumps(data), content_type="application/json")

########################Proyectos###############################

@login_required
def vista_proyectos(request):
         user = request.user
         ce= user.clavecap
         a=np.random.randint(1, 9999999)
         if request.POST:
             form = ProyectosForm(request.POST, request.FILES)
             print form
             if form.is_valid():
                 form.save()
                #messages.success(request, 'Profile details updated.')
                 return HttpResponseRedirect("/proyectos/")
         else:
             form = ProyectosForm()
         args = {}
         args.update(csrf(request))
         args['form'] = form
         listaproyectos=Proyectos.objects.all()
         return render_to_response('proyectos.html', {"form": form,"user":user,'a':a,'ce':ce,'user':user,'listaproyectos':listaproyectos})
@login_required
def vista_editar_proyectos(request,id_editarproyectos):
    editar = Proyectos.objects.get(proyectoid=id_editarproyectos)
    print editar
    if request.method == "POST":
        formulario = ProyectosForm(request.POST, instance=editar)
        if formulario.is_valid():
            formulario.save()
            return HttpResponse('<script text/javascript>alert(\'Actualización Realizada\'); window.location="/proyectos/"</script>')
            #return HttpResponseRedirect("/personas/")
            #  messages.success(request,"Usuario Actualizado!!!")
    else:
        formulario = ProyectosForm(instance=editar)
    return render_to_response('editar_proyectos.html', {"formulario": formulario})
@login_required
def vista_borrar_proyectos(request,id_borrarproyectos):
    borrar = Proyectos.objects.get(proyectoid=id_borrarproyectos)
    borrar.delete()
    # messages.success(request,"Usuario Borrado!!")
    return HttpResponseRedirect("/proyectos/")

@login_required
def vista_ajax(request):
        if request.is_ajax():
            id= request.POST['id']
            mun= Catmunicipios.objects.filter(dep=id)
            data = [{'pk': row.pk, 'mun_municipio': row.mun_municipio} for row in mun]
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            messages="No es ajax"
            return HttpResponse(messages)
@login_required
def vista_ajax_al(request):
        if request.is_ajax():
            id= request.POST['id']
            al= Cataldeas.objects.filter(idmunicipio=id)
            data = [{'idaldea': row.idaldea,'nombrealdea': row.nombrealdea} for row in al]
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            messages="No es ajax"
            return HttpResponse(messages)
    #data = serializers.serialize("xml", SomeModel.objects.all())
@login_required
def vista_ajax_ca(request):
        if request.is_ajax():
            id= request.POST['id']
            print id
            ca= Catcaserios.objects.filter(idaldea=id)
            data = [{'idcaserio': row.idcaserio,'nombrecaserio': row.nombrecaserio} for row in ca]
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            messages="No es ajax"
            return HttpResponse(messages)
    #data = serializers.serialize("xml", SomeModel.objects.all())


###########################STAFF FACILITADORES ###################################

@login_required
def vista_staff_facilitadores(request):
         user = request.user
         print user
         if request.POST:
             form = StaffFacilitadoresForm(request.POST, request.FILES)
             print form
             if form.is_valid():
                 form.save()
                 print form
                #messages.success(request, 'Profile details updated.')
                 return HttpResponseRedirect("/staff_facilitadores/")
         else:
             form = StaffFacilitadoresForm()
         args = {}
         args.update(csrf(request))
         args['form'] = form
         cuenta = Cateducadores.objects.all().count()
         user = request.user
         ce= user.clavecap
         us=user.username
         niveleducativo=Catniveleducativo.objects.all()
         estado=Catestadocivil.objects.all()
         lista=Personas.objects.filter(clavececap=ce)
         departamentos=Catdepartamentos.objects.all()
         educativa=Catopcioneseducativas.objects.all()
         material=Catmaterialdidactico.objects.all()
         modalidades=Catmodalidades.objects.all()
         tmodalidades=Cattipomodalidad.objects.all()
         proyectos=Proyectos.objects.all()
         sectores=Catsectoreseconomicos.objects.all()
         etnia=Catetnias.objects.all()
         claseeducador=Catclaseeducador.objects.all()
         nacionalidad=Catnacionalidad.objects.all()
         a=np.random.randint(1, 9999999)
         sexo=Catsexo.objects.all()
         contacts=Cateducadores.objects.all()
         grado=Catgradoalcanzado.objects.all()
         return render_to_response('staff_facilitadores.html', {"grado":grado,"contacts":contacts,"sexo":sexo,"claseeducador":claseeducador,"cuenta":cuenta,"etnia":etnia,"niveleducativo":niveleducativo,"estado":estado,"sectores":sectores,"proyectos":proyectos,"tmodalidades":tmodalidades,"modalidades":modalidades,"material":material,"educativa":educativa,"departamentos":departamentos,"form": form,"lista":lista,"ce":ce,"us":us,"a":a,"user":user,"nacionalidad":nacionalidad})
@login_required
def vista_editar_facilitadores(request,id_editarfacilitadores):
    editar = Cateducadores.objects.get(pk=id_editarfacilitadores)
    if request.method == "POST":
        formulario = StaffFacilitadoresForm(request.POST, instance=editar)
        if formulario.is_valid():
            formulario.save()
            return HttpResponse('<script text/javascript>alert(\'Actualización Realizada\'); window.location="/staff_facilitadores/"</script>')
            #  messages.success(request,"Usuario Actualizado!!!")
    else:
        formulario = StaffFacilitadoresForm(instance=editar)
    return render_to_response('editar_staff_facilitadores.html', {"formulario": formulario})
@login_required
def vista_borrar_facilitadores(request, id_borrarfacilitadores):
    borrar = Cateducadores.objects.get(pk=id_borrarfacilitadores)
    borrar.delete()
    # messages.success(request,"Usuario Borrado!!")
    return HttpResponseRedirect("/staff_facilitadores/")

@login_required
def vista_staffupdate(request):
    id=request.POST['ed_id']
    nombre=request.POST['ed_nombreeducador']
    identidad=request.POST['ed_identidad']
    sexo=request.POST['ed_sexo']
    depar=request.POST['dep']
    mun=request.POST['mun']
    aldea=request.POST['aldea']
    caserio=request.POST['caserio']
    telefono=request.POST['ed_telefono']
    correoelectronico=request.POST['ed_correoelectronico']
    etnia=request.POST['et']
    niveleeducativo=request.POST['ne']
    gradoalcanzado=request.POST['ed_gradoalcanzado']
    estadocivil=request.POST['ec']
    nacionalidad=request.POST['nac']
    fechainicio=request.POST['lasteditdate']
    fechacreacion=request.POST['creationdate']
    fechanacimiento=request.POST['fechanacimiento']
    direccion=request.POST['ed_direccion']
    categoria=request.POST['cle']
    cursor = connection.cursor()
    if  cursor.execute("UPDATE login_cateducadores SET Ed_NombreEducador = '%s',Ed_Identidad='%s',Ed_Sexo='%s',Aldea='%s',Caserio='%s',Ed_Direccion='%s',Ed_Telefono='%s',Ed_CorreoElectronico='%s',LastEditDate='%s',CreationDate='%s',FechaNacimiento='%s',Cle_Id='%s',Dep_Id='%s',EC_Id='%s',gradoalcanzado_Id='%s',Et_Id='%s',Mun_Id='%s',Nac_Id='%s',NE_Id='%s' WHERE login_cateducadores.ed_id ='%s'"%(nombre,identidad,sexo,aldea,caserio,direccion,telefono,correoelectronico,fechainicio,fechacreacion,fechanacimiento,categoria,depar,estadocivil,gradoalcanzado,etnia,mun,nacionalidad,niveleeducativo,id)):
        return HttpResponse('<script text/javascript>alert(\'Actualización Realizada\'); window.location="/staff_facilitadores/"</script>')
    else:
        return HttpResponse('<script text/javascript>alert(\'No se guardo\'); window.location="/staff_facilitadores/"</script>')









###########################Seguimiento Participantes ###################################
@login_required
def vista_seguimientoparticipantes(request):
    user = request.user
    ce = user.clavecap
    educativa=Catopcioneseducativas.objects.all()
    return render_to_response('seguimientoparticipantes.html',{"user":user,"ce":ce,"educativa":educativa})
import json
@login_required
def vista_seguimientoparametro(request):
    if request.is_ajax():
         user = request.user
         ce = user.clavecap
         idoe = request.POST['id']
         educativa=Catopcioneseducativas.objects.all()
         cursor = connection.cursor()
         #cursor.execute("UPDATE OfertaEducativa SET CD_Nombre='%s' WHERE Clave='%s'" %(a,c))
         cursor.execute("SELECT cd_nombre,ev_fechainicial,ev_fechafinal,clave  From login_catopcioneseducativas inner join login_procesoeducativo on OE_ID = opcioneducativa WHERE OE_ID = '%s' and clavececap = '%s'"%(idoe,ce))
         data = [dict(nombreproceso=row[0],idproceso=row[3])for row in cursor.fetchall()]
         return HttpResponse(json.dumps(data), content_type="application/json")
    else:
     HttpResponseRedirect("No es ajax")
@login_required
def vista_seguimientoparametro2(request):
    if request.is_ajax():
        user = request.user
        ce = user.clavecap
        idproceso = request.POST['id']
        educativa = Catopcioneseducativas.objects.all()
        cursor = connection.cursor()
        # cursor.execute("UPDATE OfertaEducativa SET CD_Nombre='%s' WHERE Clave='%s'" %(a,c))
        #cursor.execute("SELECT nombre_completo,deserto,fechadesercion,causappaldesercion,fuesometidoacertificacion,secertifico,observaciones,p_id,egreso From login_procesoeducativo inner join login_personasporprocesoeducativo  on clave=claveev  inner join login_personas on login_personas.numero_identidad = login_personasporprocesoeducativo.numero_identidad  WHERE clave='%s' and login_personas.clavececap='%s'" % (idproceso, ce))
        #cursor.execute('SELECT * FROM  login_personasporprocesoeducativo inner join login_procesoeducativo  on  login_procesoeducativo.clave=login_personasporprocesoeducativo.claveev inner join login_personas on login_personas.numero_identidad=login_personasporprocesoeducativo.numero_identidad WHERE clave="ADMIN1159012"')  
        cursor.execute("SELECT  nombre_completo,deserto,fechadesercion,causappaldesercion,fuesometidoacertificacion,secertifico,observaciones,p_id,egreso From login_procesoeducativo inner join login_personasporprocesoeducativo  on clave=claveeV  inner join login_personas on login_personas.numero_identidad= login_personasporprocesoeducativo.numero_identidad  WHERE clave='%s'" % (idproceso))

        data = [dict(nombrecompleto=row[0],deserto=row[1],fechadesercion=row[2],causa=row[3],sometido=row[4],certifico=row[5],observaciones=row[6],pk=row[7],egreso=row[8]) for row in cursor.fetchall()]
        print data
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        HttpResponseRedirect("No es ajax")
@login_required
def vista_editar_personasmatriculados(request,id_personas):
    editar = Personasporprocesoeducativo.objects.get(p_id=id_personas)



    if request.method == "POST":
        formulario = PersonasporprocesoForm(request.POST, instance=editar)
        if formulario.is_valid():
           formulario.save()
        return HttpResponse('<script text/javascript>alert(\'Actualización Realizada Personas por Proceso\'); window.location="/seguimiento_participantes/"</script>')
    else:
        formulario = PersonasporprocesoForm(instance=editar)
        return render_to_response('editar_personasporproceso.html', {"formulario": formulario})


#################################Evaluaciones###########################################
def vista_evaluaciones(request):
    user = request.user
    ce = user.clavecap
    lista=ProcesoEducativo.objects.filter(clavececap=ce)
    return render_to_response("evaluaciones.html",{'ce':ce,'user':user,'lista':lista})
def vista_evaluacion2(request,id):
    botonid=id
    user = request.user
    ce = user.clavecap
    lista = ProcesoEducativo.objects.filter(clavececap=ce)
    listap=Modulos.objects.filter(claveev__clave=id)
    return render_to_response('evaluaciones.html', {"listap": listap,'ce':ce,'user':user,'lista':lista,'botonid':botonid})
def vista_saberparticipantes(request,id_proceso):
    botonid = id_proceso
    user = request.user
    ce = user.clavecap
    lista = ProcesoEducativo.objects.filter(clavececap=ce)
    listap = Modulos.objects.filter(claveev__clave=id)
    cursor = connection.cursor()
    cursor.execute("select procesoeducativo.cd_nombre,personas.nombre_completo,personas.numero_identidad,catdepartamentos.dep_departamento,catmunicipios.mun_municipio,cataldeas.nombrealdea,catcaserios.nombrecaserio,p_id from login_personas as personas inner join  login_personasporprocesoeducativo as personasporprocesoeducativo on personas.numero_identidad=personasporprocesoeducativo.numero_identidad inner join login_procesoeducativo as procesoeducativo on procesoeducativo.clave=personasporprocesoeducativo.claveev inner join login_catdepartamentos as  catdepartamentos on catdepartamentos.dep_id=personas.dep_id inner join login_catmunicipios  as catmunicipios  on catmunicipios.dep_id=catdepartamentos.dep_id and personas.mun_id=catmunicipios.mun_id  inner join login_cataldeas  as cataldeas  on cataldeas.idmunicipio=catmunicipios.mun_id and personas.aldea=cataldeas.idaldea and cataldeas.idmunicipio=catmunicipios.mun_id inner join login_catcaserios as catcaserios  on catcaserios.idcaserio=personas.caserio and catcaserios.idaldea=cataldeas.idaldea where claveev=('%s');"%(id_proceso))
    #row=cursor.fetchall()
    #print
    entries = [dict(nombre=row[2],nombrepersona=row[1]) for row in cursor.fetchall()]
    return render_to_response('evaluaciones.html', {'listap': listap,'ce':ce,'user':user,'lista':lista,'botonid':botonid,'row':entries})
def vista_notas(request):
    try:    
        idmodulos = request.POST['idmodulos']
        idproceso = request.POST['idproceso']
    except MultiValueDictKeyError:
      return HttpResponse('<script>window.location="/evaluaciones/"</script>')
    cursor = connection.cursor()
    cursor.execute("select  login_procesoeducativo.cd_nombre,login_evaluaciones.numero_identidad,login_personas.nombre_completo,login_evaluaciones.horasteoria%s,login_evaluaciones.horaspractica%s,login_evaluaciones.notateorica%s,login_evaluaciones.notapractica%s from login_evaluaciones left join login_personas on login_evaluaciones.numero_identidad=login_personas.numero_identidad inner join login_procesoeducativo on login_procesoeducativo.clave=login_evaluaciones.claveev where login_evaluaciones.claveev='%s';"%(idmodulos,idmodulos,idmodulos,idmodulos,idproceso))
    entries = [dict(nombre=row[0],identidad=row[1],nombrecompleto=row[2],horasteoria=row[3],horapractica=row[4],notateorica=row[5],notapractica=row[6]) for row in cursor.fetchall()]
    cursor.execute("select * from vista_modulos where claveev='%s' and numero_modulo='%s';"%(idproceso,idmodulos))
    valores = [dict(modulo=row[0],nombremodulo=row[1],horasteorica=row[2],horaspractica=row[3],total_horas=row[4]) for row in cursor.fetchall()]
    #valores=cursor.fetchall()
    return render_to_response('notas.html', {'valores':valores,'entries':entries,'idmodulos':idmodulos,'idproceso':idproceso})
def vista_notasupdate(request):
    idpro=request.POST['idproceso']
    idmo=request.POST['idmodulo']
    ide=request.POST['identidad']
    hteorica = request.POST['horateorica']
    hpractica = request.POST['horapractica']
    nteorica = request.POST['notateorica']
    npractica = request.POST['notapractica']
    cursor = connection.cursor()
    a=("UPDATE login_evaluaciones SET horasteoria%s = '%s', horaspractica%s = '%s',notateorica%s = '%s',notapractica%s ='%s'WHERE login_evaluaciones.claveev ='%s' and login_evaluaciones.numero_identidad='%s'"%(idmo,hteorica,idmo,hpractica,idmo,nteorica,idmo,npractica,idpro,ide))
    cursor.execute("UPDATE login_evaluaciones SET horasteoria%s = '%s', horaspractica%s = '%s',notateorica%s = '%s',notapractica%s ='%s'WHERE login_evaluaciones.claveev ='%s' and login_evaluaciones.numero_identidad='%s'"%(idmo,hteorica,idmo,hpractica,idmo,nteorica,idmo,npractica,idpro,ide))
    return render_to_response('notas.html')



##############################MODULOS#################################################
def vista_modulos(request):
    user = request.user
    ce = user.clavecap
    us = user.username
    h="Horas Practica"
    p="Horas Teoricas"
    proceso=ProcesoEducativo.objects.filter(clavececap=ce).values('clave')
    proceso2=ProcesoEducativo.objects.filter(clavececap=ce).values('clave','Nombre_Proceso','Total_Horas')
    instructores=Cateducadores.objects.filter(clavececap=ce).values()
    horas=ProcesoEducativo.objects.filter(clavececap=ce).values('Nombre_Proceso','Total_Horas')

    for f in proceso:
        modulos = Modulos.objects.filter(claveev__in=proceso)
    if request.POST:
        form = modulosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile details updated.')
            return HttpResponseRedirect("/modulos/")
    else:
        form = modulosForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response("modulos.html",{'horas':horas,'instructores':instructores,'proceso2':proceso2,'h':h,'p':p,'proceso':proceso,'form':form,'user':user,'ce':ce,'us':us,'modulos':modulos})
def vista_modificarmodulo(request,id_proceso):
   # pro = Modulos.objects.filter(clave=id_proceso)
   # print pro
   editar = Modulos.objects.get(id=id_proceso)
   print editar
   if request.method == "POST":
       formulario = modulosForm(request.POST, instance=editar)
       if formulario.is_valid():
           formulario.save()
           return HttpResponse(
               '<script text/javascript>alert(\'Actualización Realizada\'); window.location="/modulos/"</script>')
           # return HttpResponseRedirect("/personas/")
           #  messages.success(request,"Usuario Actualizado!!!")
   else:
       formulario = modulosForm(instance=editar)
   return render_to_response('editarmodulo.html', {"formulario": formulario})


def vista_eliminarmodulo(request,id_proceso):
   # pro = Modulos.objects.filter(clave=id_proceso)
   # print pro
    try:
       borrar = Modulos.objects.get(pk=id_proceso)
       borrar.delete()
    except IntegrityError:
      return HttpResponse('<script text/javascript>alert(\'Advertencia:No se puede borrar tiene matriculados en este modulo elimine los matriculados a este modulo.\'); window.location="/modulos/"</script>')
   # messages.success(request,"Usuario Borrado!!")
    return HttpResponseRedirect("/modulos/")




#########################################################
#########CAMBIAR CONTRASEÑA##############################


@login_required
##@user_passes_test(lambda u: u.administrador)
def vista_cambiarcontrasena(request):
    user = request.user
    identidad=user.id
    editar = Perfil.objects.get(pk=identidad)
    if request.method == "POST":
        formulario = UserForm(request.POST, instance=editar)
        if formulario.is_valid():
            formulario.save()
        return HttpResponse('<script text/javascript>alert(\'Cambio Realizado\'); window.location="/"</script>')

    else:
        formulario = UserForm(instance=editar)

    return render_to_response('editar_usuarioform.html', {"formulario": formulario})


#############################################################################33
#############################################################################33
###########-----REPORTESS---------##########################################

from sie.apps.filtros.models import MasterFiltroSIE

def vista_reportes(request):
    user = request.user
    return render_to_response("reportes/reportes.html",{'user':user})

@login_required
def vista_filtro_participantes(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=1)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_participantes.html",{'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_export(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=1)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Participantes.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_participantes('%s')"%(t))
    a2 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user

    resultado = [dict(proceso=row[0], identidad=row[1], nombre=row[2],fechanacimiento=row[3], edadmeses=row[4],edadanos=row[5], edadiniciarmeses=row[6],edadiniciaranos=row[7],sexo=row[8],estaestudiando=row[9],discapacidad=row[10],departamento=row[11],mun=row[12],al=row[13],ca=row[14],deserto=row[15],fdeserto=row[16],causadesercion=row[17],etnia=row[18],nombreresponsable1=row[19],parentesco1=row[20],nombreresponsable2=row[21],parentesco2=row[22],direccion=row[23],telefono=row[24]) for row in a2]
    if  resultado:
        return render_to_response('reportes/reporte_participantes.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_participantes.html', {'user':user,'error': error})




@login_required
def vista_filtro_educadores(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=2)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_educadores.html",{'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_educadores(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=2)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Educadores.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_educadores('%s')"%(t))
    a3 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(cecap=row[0], nombre=row[1], departamento=row[2], municipio=row[3],identidad=row[4],fechanacimiento=row[5],edad=row[6], nivelescolar=row[7], grado=row[8], claseeducador=row[9],telefono=row[10], celular=row[11]) for row in a3]
    if  resultado:
        return render_to_response('reportes/reporte_educadores.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_educadores.html', {'user':user,'error': error})





@login_required
def vista_filtro_seguimiento(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=3)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_seguimiento.html",{'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_seguimiento(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=3)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Seguimiento.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_seguimiento_personas('%s')"%(t))
    a3 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(identidad=row[0], nombre=row[1], fechanacimiento=row[2], cecap=row[3],evnombre=row[4],fechafinal=row[5],totalhoras=row[6], evlugar=row[7], deserto=row[8], fechadesercion=row[9],f=row[10]) for row in a3]
    if  resultado:
        return render_to_response('reportes/reporte_seguimiento.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_seguimiento.html', {'user':user,'error': error})



@login_required
def vista_filtro_proyectos(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=4)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reportes_proyectos.html",{'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_proyectos(request):
    user = request.user
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=4)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Proyectos.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_consolidado_proyectos('%s')"%(t))
    a4 = cursor.fetchall()
    error="No Hay Información en base de Datos "

    resultado = [dict(cecap=row[0], opcioneducativa=row[1], proyecto=row[2], dep=row[3],mun=row[4],masculino=row[5],femenino=row[6],total=row[7]) for row in a4]
    if  resultado:
        return render_to_response('reportes/reportes_proyectos.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reportes_proyectos.html', {'user':user,'error': error})




@login_required
def vista_filtro_global_matricula_desercion(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=6)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_matricula_desercion.html",{'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_global_matricula_desercion(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=6)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="global_matricula_desercion.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_consolidado_global_matricula_y_desercion('%s')"%(t))
    a5 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(cecap=row[0], opcioneducativa=row[1], proceso=row[2], fechainicial=row[3],fechafinal=row[4],mujeresmi=row[5],hombresmi=row[6],totalmi=row[7],mujeresmf=row[8],hombresmf=row[9],totalmf=row[10],mujeresdeserciones=row[11],hombresdeserciones=row[12],totaldeserciones=row[13],mujeresporcentajedeserciones=row[14],hombresporcentajedeserciones=row[15],totalporcentajedeserciones=row[16]) for row in a5]
    if  resultado:
        return render_to_response('reportes/reporte_matricula_desercion.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_matricula_desercion.html', {'user':user,'error': error})



@login_required
def vista_filtro_personas_atendidas(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=7)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_personas_atendidas.html",{'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_personas_atendidas(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=7)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_personas_atendidas('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(identidad=row[0], nombre=row[1], fechanacimiento=row[2], edadmeses=row[3],edadanos=row[4],sexo=row[5],niveleducativo=row[6],departamento=row[7],municipio=row[8],aldea=row[9],caserio=row[10],etnia=row[11]) for row in a6]
    if  resultado:
        return render_to_response('reportes/reporte_personas_atendidas.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_personas_atendidas.html', {'user':user,'error': error})




@login_required
def vista_filtro_condensado_proceso(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=8)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_condensado_proceso.html",{'procesoeducativo':procesoeducativo,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_condensado_proceso(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=8)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_condensado_proceso('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(cecap=row[0], nombre=row[1], identidad=row[2], sexo=row[3],edad=row[4],niveleducativo=row[5],modulo1=row[6]
        ,modulo2=row[7],modulo3=row[8],modulo4=row[9],modulo5=row[10],modulo6=row[11],modulo7=row[12],modulo8=row[13],modulo9=row[14]
        ,modulo10=row[15],modulo11=row[16],modulo12=row[17],modulo13=row[18],modulo14=row[19],modulo15=row[20],modulo16=row[21],
        modulo17=row[22],modulo18=row[23],modulo19=row[24],modulo20=row[25],modulo21=row[26],modulo22=row[27],modulo23=row[28]
        ,modulo24=row[29],modulo25=row[30],modulo26=row[31],modulo27=row[32],modulo28=row[33]
        ,asistenciahoras=row[34],porcentajehoras=row[35],
        nota=row[36],nota2=row[37],nota3=row[38],nota4=row[39],nota5=row[40],nota6=row[41],nota7=row[42],nota8=row[43],nota9=row[44]
        ,nota10=row[45],nota11=row[46],nota12=row[47],nota13=row[48],nota14=row[49],nota15=row[50],nota16=row[51],nota17=row[52]
        ,nota18=row[53],nota19=row[54],nota20=row[55],
        nota21=row[56],nota22=row[57],nota23=row[58],nota24=row[59],nota25=row[60],nota26=row[61],nota27=row[62],nota28=row[63]
        ,valor=row[64],valor2=row[65],valor3=row[66],valor4=row[67]) for row in a6]
    
    if  resultado:
        return render_to_response('reportes/reporte_condensado_proceso.html', {'a6':a6,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_condensado_proceso.html', {'user':user,'error': error})






@login_required
def vista_filtro_pasanopasa(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=10)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_pasanopasa.html",{'procesoeducativo':procesoeducativo,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_pasanopasa(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=10)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_pasa_nopasa('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(nombre=row[0], identidad=row[1], sexo=row[2], edadanos=row[3],niveleducativo=row[4],municipio=row[5],pasanopasa=row[8],observaciones=row[9]) for row in a6]
    if  resultado:
        return render_to_response('reportes/reporte_pasanopasa.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_pasanopasa.html', {'user':user,'error': error})

@login_required
def vista_filtro_centro_formacion(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=11)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_centro_formacion.html",{'procesoeducativo':procesoeducativo,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_centro_formacion(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=11)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_centros_formacion('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(centro=row[0], opcioneducativa=row[1], OfertaEducativa=row[2], departamentos=row[3],municipio=row[4],lugarsede=row[5],masculino=row[6],femenino=row[7],total=row[8]) for row in a6]
    if  resultado:
        return render_to_response('reportes/reporte_centro_formacion.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_centro_formacion.html', {'user':user,'error': error})





@login_required
def vista_filtro_lugar(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=12)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    lugar=Cattipossedes.objects.all()
    return render_to_response("reportes/reporte_lugar.html",{'lugar':lugar,'procesoeducativo':procesoeducativo,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_lugar(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=12)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_proceso_por_lugar('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(cecap=row[0], nombre=row[1], departamento=row[2], municipio=row[3],fechainicial=row[4],fechafinal=row[5],totalhoras=row[6],modalidad=row[7],opcion=row[8],participante=row[9],lugar=row[10]) for row in a6]
    if  resultado:
        return render_to_response('reportes/reporte_lugar.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_lugar.html', {'user':user,'error': error})










@login_required
def vista_filtro_facilitador(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=13)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    educadores=Cateducadores.objects.all()
    return render_to_response("reportes/reporte_facilitador.html",{'educadores':educadores,'procesoeducativo':procesoeducativo,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_facilitador(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=13)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_cursos_por_facilitador('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(identidad=row[0], nombreeducador=row[1], nombreproceso=row[2], fechainicial=row[3],fechafinal=row[4],departamento=row[5],municipio=row[6],cecap=row[7]) for row in a6]
    if  resultado:
        return render_to_response('reportes/reporte_facilitador.html', {'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_facilitador.html', {'user':user,'error': error})





@login_required
def vista_filtro_condensado_detallado_proceso(request):
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=8)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    user = request.user
    return render_to_response("reportes/reporte_condensado_detallado_proceso.html",{'procesoeducativo':procesoeducativo,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})

@login_required
def vista_exportar_condensado_detallado_proceso(request):
    procesoeducativo=ProcesoEducativo.objects.all()
    opcioneducativa=Catopcioneseducativas.objects.all()
    nombres=Perfil.objects.filter().values('username')
    filtros = MasterFiltroSIE.objects.filter(identidicador=9)
    proyectos=Proyectos.objects.all()
    departamentos=Catdepartamentos.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM  login_perfil")
    cecaps = cursor.fetchall()
    t=request.POST.get('total')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Personas_Atendidas.csv"'
    writer = csv.writer(response)
    writer.writerow([''])
    cursor=connection.cursor()
    cursor.execute("call procedimiento_condensado_proceso_detallado('%s')"%(t))
    a6 = cursor.fetchall()
    error="No Hay Información en base de Datos "
    user = request.user
    resultado = [dict(nombre=row[1], identidad=row[2], sexo=row[3],edad=row[4],niveleducativo=row[5],nt1=row[6]
        ,ht1=row[7],np1=row[8],hp1=row[9],totalth1=row[10],totalnota1=row[11],
        nt2=row[12],ht2=row[13],np2=row[14],hp2=row[15],totalth2=row[16],totalnota2=row[17],
        nt3=row[18],ht3=row[19],np3=row[20],hp3=row[21],totalth3=row[22],totalnota3=row[23],
        nt4=row[24],ht4=row[25],np4=row[26],hp4=row[27],totalth4=row[28],totalnota4=row[29],
        nt5=row[30],ht5=row[31],np5=row[32],hp5=row[33],totalth5=row[34],totalnota5=row[35],
        nt6=row[36],ht6=row[37],np6=row[38],hp6=row[39],totalth6=row[40],totalnota6=row[41],
        nt7=row[42],ht7=row[43],np7=row[44],hp7=row[45],totalth7=row[46],totalnota7=row[47],
        nt8=row[48],ht8=row[49],np8=row[50],hp8=row[51],totalth8=row[52],totalnota8=row[53],
        nt9=row[54],ht9=row[55],np9=row[56],hp9=row[57],totalth9=row[58],totalnota9=row[59],
        nt10=row[60],ht10=row[61],np10=row[62],hp10=row[63],totalth10=row[64],totalnota10=row[65],
        nt11=row[66],ht11=row[67],np11=row[68],hp11=row[69],totalth11=row[70],totalnota11=row[71],
        nt12=row[72],ht12=row[73],np12=row[74],hp12=row[75],totalth12=row[76],totalnota12=row[77],
        nt13=row[78],ht13=row[79],np13=row[80],hp13=row[81],totalth13=row[82],totalnota13=row[83],
        nt14=row[84],ht14=row[85],np14=row[86],hp14=row[87],totalth14=row[88],totalnota14=row[89],
        nt15=row[90],ht15=row[91],np15=row[92],hp15=row[93],totalth15=row[94],totalnota15=row[95],
        nt16=row[96],ht16=row[97],np16=row[98],hp16=row[99],totalth16=row[100],totalnota16=row[101],
        nt17=row[102],ht17=row[103],np17=row[104],hp17=row[105],totalth17=row[106],totalnota17=row[107],
        nt18=row[108],ht18=row[109],np18=row[110],hp18=row[111],totalth18=row[112],totalnota18=row[113],
        nt19=row[114],ht19=row[115],np19=row[116],hp19=row[117],totalth19=row[118],totalnota19=row[119],
        nt20=row[120],ht20=row[121],np20=row[122],hp20=row[123],totalth20=row[124],totalnota20=row[125],
        nt21=row[126],ht21=row[127],np21=row[128],hp21=row[129],totalth21=row[130],totalnota21=row[131],
        nt22=row[132],ht22=row[133],np22=row[134],hp22=row[135],totalth22=row[136],totalnota22=row[137],
        nt23=row[138],ht23=row[139],np23=row[140],hp23=row[141],totalth23=row[142],totalnota23=row[143],
        nt24=row[144],ht24=row[145],np24=row[146],hp24=row[147],totalth24=row[148],totalnota24=row[149],
        nt25=row[150],ht25=row[151],np25=row[152],hp25=row[153],totalth25=row[154],totalnota25=row[155],
        nt26=row[156],ht26=row[157],np26=row[158],hp26=row[159],totalth26=row[160],totalnota26=row[161],
        nt27=row[162],ht27=row[163],np27=row[164],hp27=row[165],totalth27=row[166],totalnota27=row[167],
        nt28=row[168],ht28=row[160],np28=row[170],hp28=row[171],totalth28=row[172],totalnota28=row[173],
        ) for row in a6]
    
    if  resultado:
        return render_to_response('reportes/reporte_condensado_detallado_proceso.html', {'a6':a6,'user':user,'opcioneducativa':opcioneducativa,'procesoeducativo':procesoeducativo,'resultado':resultado,'nombres':nombres,'cecaps':cecaps,'filtros':filtros,'proyectos':proyectos,'departamentos':departamentos})
    else:
        return render_to_response('reportes/reporte_condensado_detallado_proceso.html', {'user':user,'error': error})


