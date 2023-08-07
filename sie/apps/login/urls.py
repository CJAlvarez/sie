#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..login.views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^$', vista_index, name='vista_index'),
    url(r'^auth/', vista_login, name='vista_login'),
    url(r'^dashboard/', vista_dashboard, name='vista_dashboard'),
    url(r'^close/', vista_logout, name="vista_logout"),
    # Proceso Educativo
     url(r'^proceso_educativo/', vista_proceso_educativo, name="vista_proceso_educativo"),
     url(r'^proceso_borrar/(?P<id_borrarproceso>\d+)/$', vista_borrar_proceso, name="vista_borrar_proceso"),
     url(r'^proceso_editar/(?P<id_editarproceso>\d+)/$', vista_editar_proceso, name="vista_editar_proceso"),
    # # Personas
     url(r'^personas/', vista_participantes, name="vista_participantes"),
     url(r'^personas_borrar/(?P<id_borrarparticipante>\d+)/$', vista_borrar_participantes, name="vista_borrar_participantes"),
     url(r'^personas_editar/(?P<id_editarparticipantes>\d+)/$', vista_editar_participantes, name="vista_editar_participantes"),
     url(r'^calcular/', calcular_edad, name="calcular_edad"),

    ## Matricula
    url(r'^matricula/', vista_matricula, name="vista_matricula"),
    url(r'^matricula_ajax/', vista_matricula_ajax, name="vista_matricula_ajax"),
    url(r'^matriculado_borrar/(?P<id_borrarmatriculado>(\d+))/(?P<identidad>(\d+))/(?P<clave>(\w+))/$', vista_borrar_matriculado,name="vista_borrar_matriculado"),
    url(r'^busquedamatriculado/', vista_busquedappp,name="vista_busquedappp"),

    # # Proyectos
     url(r'^proyectos/', vista_proyectos, name="vista_proyectos"),
     url(r'^proyectos_editar/(?P<id_editarproyectos>\w+)/$', vista_editar_proyectos, name="vista_editar_proyectos"),
     url(r'^proyectos_borrar/(?P<id_borrarproyectos>\w+)/$', vista_borrar_proyectos, name="vista_borrar_proyectos"),

    # #STAFF FACILITADORES
     url(r'^staff_facilitadores/', vista_staff_facilitadores, name="vista_staff_facilitadores"),
     url(r'^staff_borrar/(?P<id_borrarfacilitadores>\w+)/$', vista_borrar_facilitadores, name="vista_borrar_facilitadores"),
     url(r'^staff_editar/(?P<id_editarfacilitadores>\w+)/$', vista_editar_facilitadores, name="vista_editar_facilitadores"),
     url(r'^staff_update/', vista_staffupdate, name="vista_staffupdate"),
    url(r'^busquedaidentidad/', vista_busquedadidentidad, name="vista_busquedadidentidad"),


    #Seguimiento Participantes
    url(r'^seguimiento_participantes/', vista_seguimientoparticipantes, name="vista_seguimientoparticipantes"),
    url(r'^seguimiento_parametro/', vista_seguimientoparametro, name="vista_seguimientoparametro"),
    url(r'^seguimiento_parametro2/', vista_seguimientoparametro2, name="vista_seguimientoparametro2"),
    url(r'^modificar_personasporproceso/(?P<id_personas>\d+)/$', vista_editar_personasmatriculados, name="vista_editar_personasmatriculados"),



    #Evaluaciones
    url(r'^evaluaciones/', vista_evaluaciones, name="vista_evaluaciones"),
    url(r'^evaluacionesparametro/(?P<id>\w+)/$', vista_evaluacion2, name="vista_evaluacion2"),
    url(r'^evaluacionespproceso/(?P<id_proceso>\w+)/$', vista_saberparticipantes, name="vista_saberparticipantes"),
    url(r'^notas/', vista_notas, name="vista_notas"),
    url(r'^notasupdate/', vista_notasupdate, name="vista_notasupdate"),



    #Modulos
    url(r'^modulos/', vista_modulos, name="vista_modulos"),
    url(r'^modificarmodulo/(?P<id_proceso>\w+)/$', vista_modificarmodulo, name="vista_modificarmodulo"),
    url(r'^borrarmodulo/(?P<id_proceso>\w+)/$', vista_eliminarmodulo, name="vista_eliminarmodulo"),

    #AJAX
     url(r'^ajax/', vista_ajax, name="vista_ajax"),
     url(r'^ajax_al/', vista_ajax_al, name="vista_ajax_al"),
     url(r'^ajax_ca/', vista_ajax_ca, name="vista_ajax_ca"),

    url(r'^modificarcontrasena/', vista_cambiarcontrasena, name='vista_cambiarcontrasena'),





##############################################################################
#######################REPORTE################################################
    url(r'^reportes/', vista_reportes, name="vista_reportes"),
    url(r'^reporte_participantes/', vista_filtro_participantes, name="vista_filtro_participantes"),
    url(r'^exportar/', vista_export, name="vista_export"),
    url(r'^reporte_educadores/', vista_filtro_educadores, name="vista_filtro_educadores"),
    url(r'^exportar_educadores/', vista_exportar_educadores, name="vista_exportar_educadores"),
    url(r'^reporte_seguimiento/', vista_filtro_seguimiento, name="vista_filtro_seguimiento"),
    url(r'^exportar_seguimiento/', vista_exportar_seguimiento, name="vista_export_seguimiento"),
    url(r'^reporte_proyectos/', vista_filtro_proyectos, name="vista_filtro_proyectos"),
    url(r'^exportar_proyectos/', vista_exportar_proyectos, name="vista_exportar_proyectos"),
    url(r'^reporte_matricula_desercion/', vista_filtro_global_matricula_desercion, name="vista_filtro_global_matricula_desercion"),
    url(r'^exportar_matricula_desercion/', vista_exportar_global_matricula_desercion, name="vista_exportar_global_matricula_desercion"),
    url(r'^reporte_personas_atendidas/', vista_filtro_personas_atendidas, name="vista_filtro_personas_atendidas"),
    url(r'^exportar_personas_atendidas/', vista_exportar_personas_atendidas, name="vista_exportar_personas_atendidas"),
    url(r'^reporte_condensado_proceso/', vista_filtro_condensado_proceso, name="vista_filtro_condensado_proceso"),
    url(r'^exportar_condensado_proceso/', vista_exportar_condensado_proceso, name="vista_exportar_condensado_proceso"),
    url(r'^reporte_pasanopasa/', vista_filtro_pasanopasa, name="vista_filtro_pasanopasa"),
    url(r'^exportar_pasanopasa/', vista_exportar_pasanopasa, name="vista_exportar_pasanopasa"),
    url(r'^reporte_centro_formacion/', vista_filtro_centro_formacion, name="vista_filtro_centro_formacion"),
    url(r'^exportar_centro_formacion/', vista_exportar_centro_formacion, name="vista_exportar_centro_formacion"),
    url(r'^reporte_facilitador/', vista_filtro_facilitador, name="vista_filtro_facilitador"),
    url(r'^exportar_facilitador/', vista_exportar_facilitador, name="vista_exportar_facilitador"),
    url(r'^reporte_lugar/', vista_filtro_lugar, name="vista_filtro_lugar"),
    url(r'^exportar_lugar/', vista_exportar_lugar, name="vista_exportar_lugar"),
    url(r'^reporte_condensado_detallado_proceso/', vista_filtro_condensado_detallado_proceso, name="vista_filtro_condensado_detallado_proceso"),
    url(r'^exportar_condensado_detallado_proceso/', vista_exportar_condensado_detallado_proceso, name="vista_exportar_condensado_detallado_proceso"),    
]




   

