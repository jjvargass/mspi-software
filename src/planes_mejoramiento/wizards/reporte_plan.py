# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from openerp.exceptions import Warning, ValidationError
from openerp.addons.base_idu.tools import reportes

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

    @api.multi
    def crear_reporte_plan(self):
        all_data = []
        plan = {}
        # construir diccionario
        plan['plan_id'] = self.plan_id.id or ''
        plan['plan_fecha'] = self.plan_id.fecha or ''
        plan['plan_origen'] = self.plan_id.origen_id.name or ''
        plan['plan_sub_origen'] = self.plan_id.sub_origen_id.name or ''
        plan['plan_unidad'] = self.plan_id.dependencia_id.name or ''
        plan['plan_usuario'] = self.plan_id.user_id.name or ''
        plan['plan_radicado'] = self.plan_id.radicado or ''
        if (self.plan_id.hallazgo_ids):
            for hallazgo in self.plan_id.hallazgo_ids:
                plan['hallazgo_nombre'] = self.hallazgo.name or ''
                plan['hallazgo_nombre'] = self.hallazgo.name or ''
                plan['hallazgo_unidad'] = self.hallazgo.dependencia_id or ''
                if (hallazgo.acciones_ids):
                    for accion in hallazgo.acciones_ids:
                        plan['accion_descripcion'] = self.accion.descripcion or ''
                else:
                    print "vacio accion"
                    print "vacio avance"
        else:
            print "vacio hallazgo"
            print "vacio accion"
            print "vacio avance"

        # crear reporte
        documento = reportes.crear_reporte(
            self,
            proyecto,
            'PLAN_INTERNO',
            'xls',
            'plan_interno.ods',
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
        print view_ids
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
