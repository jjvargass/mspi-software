# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from openerp.exceptions import Warning, ValidationError
from openerp.addons.base_idu.tools import reportes
from reportlab.lib.textsplit import ALL_CANNOT_END

TIPO_PLAN = [
    ('interno', 'Interno'),
    ('contraloria_bog', 'Contraloría de Bogotá'),
    ('contraloria_gral', 'Contraloría General'),
]

class plan_mejoramientos_wizard_reporte_plan(models.TransientModel):
    _name = 'plan_mejoramiento.wizard.reporte_plan'

    # -------------------
    # Fields
    # -------------------
    archivo = fields.Binary('Archivo',readonly=True,filters="xls")
    nombre_archivo = fields.Char('Nombre del Archivo', size=255)

    tipo = fields.Selection(
        TIPO_PLAN,
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Topo''',
    )
    plan_id = fields.Many2one(
        string='Plan de Mejoramiento',
        required=True,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.plan',
        ondelete='restrict',
        help='''Plan de Mejoramiento''',
        domain="[('tipo','=',tipo)]",
    )

    # -------------------
    # methods
    # -------------------

    def definir_plan(self, dic_plan, obj_plan={}):
        if obj_plan:
            dic_plan['plan_id'] = obj_plan.id or ''
            dic_plan['plan_nombre'] = obj_plan.name or ''
            dic_plan['plan_fecha'] = obj_plan.fecha or ''
            dic_plan['plan_origen'] = obj_plan.origen_id.name or ''
            dic_plan['plan_sub_origen'] = obj_plan.sub_origen_id.name or ''
            dic_plan['plan_unidad'] = obj_plan.dependencia_id.name or ''
            dic_plan['plan_usuario'] = obj_plan.user_id.name or ''
            dic_plan['plan_radicado'] = obj_plan.radicado or ''
        else:
            dic_plan['plan_id'] = ''
            dic_plan['plan_nombre'] = ''
            dic_plan['plan_fecha'] = ''
            dic_plan['plan_origen'] = ''
            dic_plan['plan_sub_origen'] = ''
            dic_plan['plan_unidad'] = ''
            dic_plan['plan_usuario'] = ''
            dic_plan['plan_radicado'] = ''

    def definir_hallazgo(self, dic_hallazgo, obj_hallazgo={}):
        if obj_hallazgo:
            dic_hallazgo['hallazgo_nombre'] = obj_hallazgo.name or ''
            dic_hallazgo['hallazgo_descripcion'] = obj_hallazgo.descripcion or ''
            dic_hallazgo['hallazgo_unidad'] = obj_hallazgo.dependencia_id.name or ''
            dic_hallazgo['hallazgo_causa'] = self.consolidar_causa (obj_hallazgo.causa_ids) or ''
        else:
            dic_hallazgo['hallazgo_nombre'] = ''
            dic_hallazgo['hallazgo_descripcion'] = ''
            dic_hallazgo['hallazgo_unidad'] = ''
            dic_hallazgo['hallazgo_causa'] = ''

    def definir_accion(self, dic_accion, obj_accion={}):
        if obj_accion:
            dic_accion['accion_nombre'] = obj_accion.name or ''
            dic_accion['accion_descripcion'] = obj_accion.descripcion or ''
            dic_accion['accion_tipo'] = obj_accion.tipo or ''
            dic_accion['accion_objetivo'] = obj_accion.objetivo or ''
            dic_accion['accion_indicador'] = obj_accion.indicador or ''
            dic_accion['accion_meta'] = obj_accion.meta or ''
            dic_accion['accion_unidad_medida'] = obj_accion.unidad_medida or ''
            dic_accion['accion_unidad'] = obj_accion.dependencia_id.name or ''
            dic_accion['accion_recursos'] = self.consolidar_recurso(obj_accion.recurso_ids) or ''
            dic_accion['accion_fecha_inicio'] = obj_accion.fecha_inicio or ''
            dic_accion['accion_fecha_fin'] = obj_accion.fecha_inicio or ''
            dic_accion['accion_estado'] = obj_accion.state or ''
            dic_accion['accion_ejecutor'] = obj_accion.ejecutor_id.name or ''
        else:
            dic_accion['accion_nombre'] = ''
            dic_accion['accion_descripcion'] = ''
            dic_accion['accion_tipo'] = ''
            dic_accion['accion_objetivo'] = ''
            dic_accion['accion_indicador'] = ''
            dic_accion['accion_meta'] = ''
            dic_accion['accion_unidad_medida'] = ''
            dic_accion['accion_unidad'] = ''
            dic_accion['accion_recursos'] = ''
            dic_accion['accion_fecha_inicio'] = ''
            dic_accion['accion_fecha_fin'] = ''
            dic_accion['accion_estado'] = ''
            dic_accion['accion_ejecutor'] = ''

    def definir_avance(self, dic_avance, obj_avance={}):
        if obj_avance:
            dic_avance['avance_descripcion'] = obj_avance.descripcion or ''
            dic_avance['avance_state'] = obj_avance.state or ''
            dic_avance['avance_calificacion'] = obj_avance.tipo_calificacion_id.name or ''
            dic_avance['avance_porcentaje_avance'] = obj_avance.porcentaje_avance or ''
            dic_avance['avance_observacion'] = obj_avance.observacion or ''
            dic_avance['avance_fecha_creacion'] = obj_avance.fecha_creacion or ''
        else:
            dic_avance['avance_descripcion'] = ''
            dic_avance['avance_state'] = ''
            dic_avance['avance_calificacion'] = ''
            dic_avance['avance_porcentaje_avance'] = ''
            dic_avance['avance_observacion'] = ''
            dic_avance['avance_fecha_creacion'] = ''

    def avance_actual(self, plan_id, plan_tipo, accion_id):
        # visitas = self.env['urbanizadores.proyecto.visita'].search([('proyecto_id', '=', proyecto.id)])
        avance_max = self.env['plan_mejoramiento.avance'].search(
            [
                ('plan_id', '=', plan_id),
                ('plan_tipo', '=', plan_tipo),
                ('accion_id', '=', accion_id),
            ],
            order='fecha_creacion DESC',
            limit=1,
        )
        return avance_max

    def consolidar_causa(self, causa_ids):
        all_causa = ''
        for causa in causa_ids:
            all_causa = all_causa + causa.name + ', '
        return all_causa

    def consolidar_recurso(self, recurso_ids):
        all_recurso = ''
        for recurso in recurso_ids:
            all_recurso = all_recurso + recurso.name + ', '
        return all_recurso

    @api.multi
    def crear_reporte_plan(self):
        all_data = []
        # construir diccionario
        if (self.plan_id.hallazgo_ids):
            for hallazgo in self.plan_id.hallazgo_ids:
                plan = {}
                if (hallazgo.accion_ids):
                    for accion in hallazgo.accion_ids:
                        if(accion.avance_ids):
                            if (len(accion.avance_ids) >= 2):
                                avance_max = self.avance_actual(self.plan_id.id, self.plan_id.tipo, accion.id)
                            else:
                                avance_max = accion.avance_ids
                            self.definir_plan(plan, self.plan_id)
                            self.definir_hallazgo(plan, hallazgo)
                            self.definir_accion(plan, accion)
                            self.definir_avance(plan, avance_max)
                            all_data.append(plan)
                            plan = {}
                        else:
                            self.definir_plan(plan, self.plan_id)
                            self.definir_hallazgo(plan, hallazgo)
                            self.definir_accion(plan, accion)
                            self.definir_avance(plan)
                            all_data.append(plan)
                            plan = {}
                else:
                    self.definir_plan(plan, self.plan_id)
                    self.definir_hallazgo(plan, hallazgo)
                    self.definir_accion(plan)
                    self.definir_avance(plan)
                    all_data.append(plan)
                    plan = {}
        else:
            self.definir_plan(plan, self.plan_id)
            self.definir_hallazgo(plan)
            self.definir_accion(plan)
            self.definir_avance(plan)
            all_data.append(plan)
            plan = {}

        if (self.tipo == 'interno'):
            # crear reporte
            documento = reportes.crear_reporte(
                self,
                all_data,
                'PLAN_INTERNO',
                'xls',
                'plan_interno.ods',
                'plan_mejoramiento_ruta_plantilla_reportes'
            )
        elif (self.tipo == 'contraloria_bog'):
            documento = reportes.crear_reporte(
                self,
                all_data,
                'PLAN_BOGOTA',
                'xls',
                'plan_bogota.ods',
                'plan_mejoramiento_ruta_plantilla_reportes'
            )
        elif (self.tipo == 'contraloria_gral'):
            documento = reportes.crear_reporte(
                self,
                all_data,
                'PLAN_GENERAL',
                'xls',
                'plan_general.ods',
                'plan_mejoramiento_ruta_plantilla_reportes'
            )

        # eliminar imagenes
        reportes.limpiar_carpeta('/tmp/img_reporte')
        # nombre del reporte para campos de odoo
        self.archivo = documento[0]
        self.nombre_archivo = documento[1]
        # buscamos el wizar de descarga
        view_ids = self.env['ir.ui.view'].search([('model','=','plan_mejoramiento.wizard.reporte_plan'),
                                                  ('name','=','plan_mejoramiento.wizard.reporte_plan_download')])
        ids = self.id
        return {
                'view_type':'form',
                'view_mode':'form',
                'res_model':'plan_mejoramiento.wizard.reporte_plan',
                'target':'new',
                'type':'ir.actions.act_window',
                'view_id':view_ids.id,
                'res_id': ids
        }
