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
         cuenta = ProcesoEducativo.objects.all().count()
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
         user = request.user
         ce= user.clavecap
         us=user.username
         lista=ProcesoEducativo.objects.filter(clavececap=ce)
         paginator = Paginator(lista,10000)  # Show 25 contacts per page

         page = request.GET.get('page')
         try:
             contacts = paginator.page(page)
         except PageNotAnInteger:
             # If page is not an integer, deliver first page.
             contacts = paginator.page(1)
         except EmptyPage:
             # If page is out of range (e.g. 9999), deliver last page of results.
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
       borrar = ProcesoEducativo.objects.get(cecap_id=id_borrarproceso)
       borrar.delete()
       #messages.success(request,"Usuario Borrado!!")
       return HttpResponseRedirect("/proceso_educativo/")
@login_required
def vista_editar_proceso(request,id_editarproceso):
    editar = ProcesoEducativo.objects.get(cecap_id=id_editarproceso)
    if request.method == "POST":
        formulario = ProcesoForm(request.POST, instance=editar)
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
         lista=Personas.objects.filter(clavececap=ce)
         paginator = Paginator(lista, 10000)  # Show 25 contacts per page

         page = request.GET.get('page')
         try:
             contacts = paginator.page(page)
         except PageNotAnInteger:
             # If page is not an integer, deliver first page.
             contacts = paginator.page(1)
         except EmptyPage:
             # If page is out of range (e.g. 9999), deliver last page of results.
             contacts = paginator.page(paginator.num_pages)
         departamentos=Catdepartamentos.objects.all()
         educativa=Catopcioneseducativas.objects.all()
         material=Catmaterialdidactico.objects.all()
         modalidades=Catmodalidades.objects.all()
         tmodalidades=Cattipomodalidad.objects.all()
         proyectos=Proyectos.objects.all()
         sectores=Catsectoreseconomicos.objects.all()
         etnia=Catetnias.objects.all()
         a=np.random.randint(1, 9999999)
         print cuenta
         return render_to_response('personas.html', {"contacts":contacts,"cuenta":cuenta,"etnia":etnia,"niveleducativo":niveleducativo,"estado":estado,"sectores":sectores,"proyectos":proyectos,"tmodalidades":tmodalidades,"modalidades":modalidades,"material":material,"educativa":educativa,"departamentos":departamentos,"form": form,"lista":lista,"ce":ce,"us":us,"a":a,"user":user})
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
#@login_required
#def vista_string_participantes(request):
#    a = request.POST.get('nombre')
#    c =request.POST.get('clave')
#    cursor = connection.cursor()
#    cursor.execute("UPDATE OfertaEducativa SET CD_Nombre='%s' WHERE Clave='%s'" %(a,c))
#    cursor.commit()
#    cursor.close()
#    return HttpResponseRedirect("/oferta_educativa/")

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
@login_required
def vista_matricula_ajax(request):
    if request.method == "POST":
       try:
        c = request.POST['clave']
        i = request.POST.getlist('videntidad')
        #    print c 
         #   print i 
        except MultiValueDictKeyError:
            return HttpResponse('<script text/javascript>alert(\'Ingrese un Valor Valido\'); window.location="/matricula/"</script>')
        cursor = connection.cursor()
        try:
            for t in i:
                lista = ''.join(t)
                cursor.execute("INSERT INTO login_personasporprocesoeducativo(claveev,numero_identidad) VALUES('%s','%s');" % (c,lista))
               cursor.execute("INSERT INTO login_evaluaciones(numero_identidad,claveev,clave)VALUES('%s','%s','1');"%(lista,c))
        except IntegrityError:
            return HttpResponse('<script text/javascript>alert(\'Ya Esta Registrado\'); window.location="/matricula/"</script>')
    return HttpResponse('<script text/javascript>alert(\'Exitosamente Matriculado\'); window.location="/matricula/"</script>')
@login_required
def vista_matricula(request):
    user = request.user
    ce = user.clavecap
    personas=Personas.objects.all()
    lista = ProcesoEducativo.objects.filter(clavececap=ce)
    cursor = connection.cursor()
    cursor.execute("select procesoeducativo.cd_nombre,personas.nombre_completo,personas.numero_identidad,catdepartamentos.dep_departamento,catmunicipios.mun_municipio,cataldeas.nombrealdea,catcaserios.nombrecaserio,p_id from login_personas as personas inner join  login_personasporprocesoeducativo as personasporprocesoeducativo on personas.numero_identidad=personasporprocesoeducativo.numero_identidad inner join login_procesoeducativo as procesoeducativo on procesoeducativo.clave=personasporprocesoeducativo.claveev inner join login_catdepartamentos as  catdepartamentos on catdepartamentos.dep_id=personas.dep_id inner join login_catmunicipios  as catmunicipios  on catmunicipios.dep_id=catdepartamentos.dep_id and personas.mun_id=catmunicipios.mun_id  inner join login_cataldeas  as cataldeas  on cataldeas.idmunicipio=catmunicipios.mun_id and personas.aldea=cataldeas.idaldea and cataldeas.idmunicipio=catmunicipios.mun_id inner join login_catcaserios as catcaserios  on catcaserios.idcaserio=personas.caserio and catcaserios.idaldea=cataldeas.idaldea")
    entries = [dict(title=row[0], text=row[1],identidad=row[2],dep=row[3],mun=row[4],al=row[5],ca=row[6],id=row[7]) for row in cursor.fetchall()]
    contexto={'personas': personas,'ce':ce,'user':user,'lista':lista,'row':entries,}
    return render(request,"matricula.html",contexto)
@login_required
def vista_borrar_matriculado(request,id_borrarmatriculado,identidad,clave):
        print id_borrarmatriculado
        print  identidad
        print clave
        borrar = Personasporprocesoeducativo.objects.get(p_id=id_borrarmatriculado)
        print borrar
        borrar.delete()
        user = request.user
        ce = user.clavecap
        lista = ProcesoEducativo.objects.filter(clavececap=ce).values("clave")
        print lista
        borrarnota=Evaluaciones.objects.filter(claveev=clave,numero_identidad=identidad).delete()
        print borrarnota
@login_required
def vista_busquedappp(request):
    if request.is_ajax():
        b = request.POST['id']
        cursor = connection.cursor()
        cursor.execute("select procesoeducativo.cd_nombre,personas.nombre_completo,personas.numero_identidad,catdepartamentos.dep_departamento,catmunicipios.mun_municipio,cataldeas.nombrealdea,catcaserios.nombrecaserio,p_id,claveev from login_personas as personas inner join  login_personasporprocesoeducativo as personasporprocesoeducativo on personas.numero_identidad=personasporprocesoeducativo.numero_identidad inner join login_procesoeducativo as procesoeducativo on procesoeducativo.clave=personasporprocesoeducativo.claveev inner join login_catdepartamentos as  catdepartamentos on catdepartamentos.dep_id=personas.dep_id inner join login_catmunicipios  as catmunicipios  on catmunicipios.dep_id=catdepartamentos.dep_id and personas.mun_id=catmunicipios.mun_id  inner join login_cataldeas  as cataldeas  on cataldeas.idmunicipio=catmunicipios.mun_id and personas.aldea=cataldeas.idaldea and cataldeas.idmunicipio=catmunicipios.mun_id inner join login_catcaserios as catcaserios  on catcaserios.idcaserio=personas.caserio and catcaserios.idaldea=cataldeas.idaldea WHERE claveev LIKE ('%s');" % (b))
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
         return render_to_response('staff_facilitadores.html', {"contacts":contacts,"sexo":sexo,"claseeducador":claseeducador,"cuenta":cuenta,"etnia":etnia,"niveleducativo":niveleducativo,"estado":estado,"sectores":sectores,"proyectos":proyectos,"tmodalidades":tmodalidades,"modalidades":modalidades,"material":material,"educativa":educativa,"departamentos":departamentos,"form": form,"lista":lista,"ce":ce,"us":us,"a":a,"user":user,"nacionalidad":nacionalidad})
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
         cursor.execute("SELECT CD_Nombre,EV_Fechainicial,EV_FechaFinal,clave  From login_Catopcioneseducativas inner join login_ProcesoEducativo on OE_ID = OpcionEducativa WHERE OE_ID = '%s' and ClaveCecap = '%s'"%(idoe,ce))
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
        cursor.execute("SELECT  Nombre_Completo,Deserto,FechaDesercion,CausaPpalDesercion,FueSometidoACertificacion,SeCertifico,Observaciones,p_id  From login_ProcesoEducativo inner join login_Personasporprocesoeducativo  on Clave=ClaveEV  inner join login_Personas on login_Personas.numero_identidad= login_Personasporprocesoeducativo.numero_identidad  WHERE CLave='%s' and login_Personas.ClaveCecap='%s'" % (idproceso, ce))
        data = [dict(nombrecompleto=row[0],deserto=row[1],fechadesercion=row[2],causa=row[3],sometido=row[4],certifico=row[5],observaciones=row[6],pk=row[7]) for row in cursor.fetchall()]
        print data
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        HttpResponseRedirect("No es ajax")
@login_required
def vista_editar_personasmatriculados(request,id_personas):
    editar = Personasporprocesoeducativo.objects.get(p_id=id_personas)
    if request.method == "POST":
        formulario = PersonasporprocesoForm(request.POST, instance=editar)
        print formulario
        if formulario.is_valid():
           formulario.save()
           print formulario
           return HttpResponse('<script text/javascript>alert(\'Actualización Realizada\'); window.location="/seguimiento_participantes/"</script>')

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
    print type(listap)
    return render_to_response('evaluaciones.html', {"listap": listap,'ce':ce,'user':user,'lista':lista,'botonid':botonid})
def vista_saberparticipantes(request,id_proceso):
    botonid = id_proceso
    user = request.user
    ce = user.clavecap
    lista = ProcesoEducativo.objects.filter(clavececap=ce)
    listap = Modulos.objects.filter(claveev__clave=id)
    cursor = connection.cursor()
    cursor.execute("select ProcesoEducativo.CD_Nombre,Personas.Nombre_Completo,Personas.Numero_identidad,CatDepartamentos.Dep_Departamento,CatMunicipios.Mun_Municipio,CatAldeas.NombreAldea,CatCaserios.NombreCaserio,P_id from login_Personas as Personas inner join  login_PersonasPorProcesoEducativo as PersonasPorProcesoEducativo on Personas.Numero_identidad=PersonasPorProcesoEducativo.Numero_identidad inner join login_ProcesoEducativo as ProcesoEducativo on ProcesoEducativo.Clave=PersonasPorProcesoEducativo.ClaveEV inner join login_CatDepartamentos as  CatDepartamentos on CatDepartamentos.Dep_Id=Personas.Dep_Id inner join login_CatMunicipios  as CatMunicipios  on CatMunicipios.Dep_Id=CatDepartamentos.Dep_Id and personas.Mun_id=CatMunicipios.Mun_Id  inner join login_CatAldeas  as CatAldeas  on CatAldeas.IdMunicipio=CatMunicipios.Mun_Id and Personas.Aldea=CatAldeas.IdAldea and CatAldeas.IdMunicipio=CatMunicipios.Mun_Id inner join login_CatCaserios as CatCaserios  on CatCaserios.IdCaserio=Personas.Caserio and CatCaserios.IdAldea=CatAldeas.IdAldea WHERE ClaveEv=('%s');"%(id_proceso))
    #row=cursor.fetchall()
    #print
    entries = [dict(nombre=row[2],nombrepersona=row[1]) for row in cursor.fetchall()]
    return render_to_response('evaluaciones.html', {'listap': listap,'ce':ce,'user':user,'lista':lista,'botonid':botonid,'row':entries})
def vista_notas(request):
    idmodulos = request.POST['idmodulos']
    idproceso = request.POST['idproceso']
    cursor = connection.cursor()
    cursor.execute("select  login_ProcesoEducativo.CD_Nombre,login_Evaluaciones.Numero_identidad,login_personas.Nombre_Completo,login_Evaluaciones.HorasTeoria%s,login_Evaluaciones.HorasPractica%s,login_Evaluaciones.NotaTeorica%s,login_Evaluaciones.NotaPractica%s from login_Evaluaciones left join login_personas on login_Evaluaciones.Numero_identidad=login_Personas.Numero_identidad inner join login_ProcesoEducativo on login_ProcesoEducativo.Clave=login_Evaluaciones.ClaveEV where login_Evaluaciones.ClaveEV='%s';"%(idmodulos,idmodulos,idmodulos,idmodulos,idproceso))
    entries = [dict(nombre=row[0],identidad=row[1],nombrecompleto=row[2],horasteoria=row[3],horapractica=row[4],notateorica=row[5],notapractica=row[6]) for row in cursor.fetchall()]
    return render_to_response('notas.html', {'entries':entries,'idmodulos':idmodulos,'idproceso':idproceso})
def vista_notasupdate(request):
    idpro=request.POST['idproceso']
    idmo=request.POST['idmodulo']
    ide=request.POST['identidad']
    hteorica = request.POST['horateorica']
    hpractica = request.POST['horapractica']
    nteorica = request.POST['notateorica']
    npractica = request.POST['notapractica']
    print ide,hpractica,hteorica,nteorica,npractica,idpro,idmo
    cursor = connection.cursor()
    a=("UPDATE login_evaluaciones SET HorasTeoria%s = '%s', HorasPractica%s = '%s',NotaTeorica%s = '%s',NotaPractica%s ='%s'WHERE login_Evaluaciones.ClaveEV ='%s' and login_evaluaciones.numero_identidad='%s'"%(idmo,hteorica,idmo,hpractica,idmo,nteorica,idmo,npractica,idpro,ide))
    print a
    cursor.execute("UPDATE login_evaluaciones SET HorasTeoria%s = '%s', HorasPractica%s = '%s',NotaTeorica%s = '%s',NotaPractica%s ='%s'WHERE login_Evaluaciones.ClaveEV ='%s' and login_evaluaciones.numero_identidad='%s'"%(idmo,hteorica,idmo,hpractica,idmo,nteorica,idmo,npractica,idpro,ide))
    return render_to_response('notas.html')



##############################MODULOS#################################################
def vista_modulos(request):
    user = request.user
    ce = user.clavecap
    us = user.username
    proceso=ProcesoEducativo.objects.filter(clavececap=ce).values('clave')
    for f in proceso:
        modulos = Modulos.objects.filter(claveev__in=proceso)
    if request.POST:
        form = modulosForm(request.POST, request.FILES)
        print form
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile details updated.')
            return HttpResponseRedirect("/modulos/")
    else:
        form = modulosForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response("modulos.html",{'proceso':proceso,'form':form,'user':user,'ce':ce,'us':us,'modulos':modulos})
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
   borrar = Modulos.objects.get(pk=id_proceso)
   borrar.delete()
   # messages.success(request,"Usuario Borrado!!")
   return HttpResponseRedirect("/modulos/")
