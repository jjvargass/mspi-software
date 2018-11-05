# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from openerp.exceptions import Warning, ValidationError
from openerp.addons.base_idu.tools import reportes
from reportlab.lib.textsplit import ALL_CANNOT_END

class activo_informacion_wizard_reporte_activo(models.TransientModel):
    _name = 'activo_informacion.wizard.reporte_activo'

    # -------------------
    # Fields
    # -------------------
    archivo = fields.Binary('Archivo',readonly=True,filters="xls")
    nombre_archivo = fields.Char('Nombre del Archivo', size=255)

    proceso_id = fields.Many2one(
        string='Proceso',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_proceso.proceso',
        ondelete='restrict',
        help='''Proceso''',
    )


    # -------------------
    # methods
    # -------------------

    def definir_estructura_dic(self, dic_activo, obj_activo):
        dic_activo['id'] = obj_activo.id or ''
        dic_activo['proceso'] = obj_activo.proceso_id.name or ''
        dic_activo['nombre'] = obj_activo.name or ''
        dic_activo['descripcion'] = obj_activo.descripcion or ''
        dic_activo['tipo'] = obj_activo.tipo.name or ''
        dic_activo['ubicacion_fisica'] = obj_activo.company_location_id.name or ''
        dic_activo['ubicacion_logica'] = obj_activo.ubicacion_logica or ''
        dic_activo['confidencialidad'] = obj_activo.confidencialidad or ''
        dic_activo['integridad'] = obj_activo.integridad or ''
        dic_activo['disponibilidad'] = obj_activo.disponibilidad or ''
        dic_activo['confidencialidad_just'] = obj_activo.confidencialidad_justificacion or ''
        dic_activo['integridad_just'] = obj_activo.integridad_justificacion or ''
        dic_activo['disponibilidad_just'] = obj_activo.disponibilidad_justicicacion or ''
        dic_activo['criticidad'] = obj_activo.criticidad or ''
        dic_activo['propietaio'] = obj_activo.propietario_dependencia_id.name or ''
        dic_activo['custodio'] = obj_activo.custodio_dependencia_id.name or ''
        dic_activo['acceso'] = obj_activo.acceso_id.name or ''
        dic_activo['fecha_registro'] = obj_activo.fecha_creacion or ''
        dic_activo['fecha_ingreso'] = obj_activo.fecha_ingreso or ''
        dic_activo['fecha_retiro'] = obj_activo.fecha_retiro or ''
        dic_activo['estado'] = obj_activo.state or ''

    @api.multi
    def crear_reporte_activo(self):
        all_data = []
        # Activos por proceso
        activos = self.env['activo_informacion.activo'].search([
            #('state', '=', 'publicado'),
            ('proceso_id', '=', self.proceso_id.id),
        ],order="propietario_dependencia_id, custodio_dependencia_id")
        # construir diccionario
        for activo in activos:
            activo_dic = {}
            self.definir_estructura_dic(activo_dic, activo)
            all_data.append(activo_dic)

        # crear reporte
        documento = reportes.crear_reporte(
            self,
            all_data,
            'INVENTARIO_ACTIVO_INFORMACION',
            'xls',
            'activo_informacion.ods',
            'activo_informacion_ruta_plantilla_reportes'
        )

        # eliminar imagenes
        reportes.limpiar_carpeta('/tmp/img_reporte')
        # nombre del reporte para campos de odoo
        self.archivo = documento[0]
        self.nombre_archivo = documento[1]
        # buscamos el wizar de descarga
        view_ids = self.env['ir.ui.view'].search([('model','=','activo_informacion.wizard.reporte_activo'),
                                                  ('name','=','activo_informacion.wizard.reporte_activo_download')])
        ids = self.id
        return {
                'view_type':'form',
                'view_mode':'form',
                'res_model':'activo_informacion.wizard.reporte_activo',
                'target':'new',
                'type':'ir.actions.act_window',
                'view_id':view_ids.id,
                'res_id': ids
        }
