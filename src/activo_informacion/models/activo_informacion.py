# -*- coding: utf-8 -*-
##############################################################################
#
#    JOSÉ JAVIER VARGAS SERRATO <https://jotavargas.github.io/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from _cffi_backend import string


TIPO_ACTIVO = [
    ('informacion', 'Información'),
    ('software', 'Software'),
    ('recurso_humano', 'Recurso Humano'),
    ('servicio', 'Servicio'),
    ('hardware', 'Hardware'),
    ('otros', 'Otros'),
]

class activo_informacion_activo_tipo(models.Model):
    _name = 'activo_informacion.activo_tipo'
    _description = 'Tipo Activo de Información'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    activo_sistema = fields.Boolean(
        string='Habilitado en el sistema',
        track_visibility='onchange',
        help='''Habilitado en el sistema''',
        default=True,
    )
    name = fields.Char(
        string='Nombre',
        required=True,
        track_visibility='onchange',
        size=255,
        help='''Nombre''',
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción''',
    )
    tipo = fields.Selection(
        TIPO_ACTIVO,
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Tipo''',
    )

    # -------------------
    # methods
    # -------------------

class activo_informacion_activo(models.Model):
    _name = 'activo_informacion.activo'
    _description = 'Activos de Información'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    name = fields.Char(
        string='Nombre',
        required=True,
        track_visibility='onchange',
        size=255,
        help='''Nombre''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    proceso_id = fields.Many2one(
        string='Proceso',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_proceso.proceso',
        ondelete='restrict',
        help='''Proceso''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )

    propietario_dependencia_id = fields.Many2one(
        string='Unidad Propietario',
        required=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad Propietario''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    propietario_id = fields.Many2one(
        string='Propietario',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='propietario_dependencia_id.manager_id.user_id',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Propietario''',
    )

    custodio_dependencia_id = fields.Many2one(
        string='Unidad Custodio',
        required=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad Custodio''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    custodio_id = fields.Many2one(
        string='Custodio',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='custodio_dependencia_id.manager_id.user_id',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Custodio''',
    )

    tipo_para_busqueda = fields.Selection(
        TIPO_ACTIVO,
        string='Tipo',
        required=True,
        track_visibility='onchange',
        store=True,
        help='''Tipo''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    tipo = fields.Many2one(
        domain="[('tipo','=', tipo_para_busqueda)]",
        string='Detalle Tipo',
        required=True,
        track_visibility='onchange',
        comodel_name='activo_informacion.activo_tipo',
        ondelete='restrict',
        help='''Detalle Tipo''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    # ubicacion fisica
    ubicacion_fisica = fields.Char(
        string='Ubicación Fisica',
        required=True,
        track_visibility='onchange',
        help='''Ubicación''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    company_location_id = fields.Many2one(
        string='Sede',
        comodel_name='res.company.location',
        ondelete='restrict',
        readonly=True,
        track_visibility='onchange',
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    company_location_piso = fields.Integer(
        string='Piso',
        readonly=True,
        track_visibility='onchange',
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    # ubicacion logica
    ubicacion_logica = fields.Char(
        string='Ubicación Lógica',
        required=True,
        track_visibility='onchange',
        help='''Ubicación''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    user_id = fields.Many2one(
        string='Registrador',
        required=True,
        readonly=True,
        track_visibility='onchange',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Ejecutor''',
        default=lambda self: self._context.get('uid', self.env['res.users'].browse()),
    )
    dependencia_id = fields.Many2one(
        string='Unidad Registrador',
        required=False,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad''',
        readonly=True,
        default=lambda self: self.env.user.department_id.id,
    )
    confidencialidad = fields.Selection(
        string='Confidencialidad',
        required=True,
        track_visibility='onchange',
        help='''Confidencialidad''',
        selection=[
            ('IPR', 'Información Publica Reservada - IPR'),
            ('IPC', 'Información Publica Clasificada - IPC'),
            ('IPB', 'Información Publica - IPB'),
        ],
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    confidencialidad_justificacion = fields.Text(
        string='Justificación Confidencialidad',
        required=True,
        track_visibility='onchange',
        help='''describe el impacto que causaría la pérdida de la confidencialidad''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    integridad = fields.Selection(
        string='Integridad',
        required=True,
        track_visibility='onchange',
        help='''Integridad''',
        selection=[
            ('A', 'ALTA'),
            ('M', 'MEDIA'),
            ('B', 'BAJA'),
        ],
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    integridad_justificacion = fields.Text(
        string='Justificación Integridad',
        required=True,
        track_visibility='onchange',
        help='''describe el impacto que causaría la pérdida de la Integridad''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    disponibilidad = fields.Selection(
        string='Disponibilidad',
        required=True,
        track_visibility='onchange',
        help='''Disponibilidad''',
        selection=[
            ('1', 'ALTA'),
            ('2', 'MEDIA'),
            ('3', 'BAJA'),
        ],
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    disponibilidad_justicicacion = fields.Text(
        string='Justificación Disponibilidad',
        required=True,
        track_visibility='onchange',
        help='''describe el impacto que causaría la pérdida de la disponibilidad''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    criticidad = fields.Char(
        string='Criticidad',
        required=False,
        readonly=True,
        track_visibility='onchange',
        size=255,
        help='''Valor general del Activo''',
    )
    fecha_creacion = fields.Date(
        string='Fecha Registro',
        required=False,
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Registro''',
        default=fields.Date.today,
    )
    fecha_ingreso = fields.Date(
        string='Fecha Ingreso',
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Ingreso''',
    )
    fecha_retiro = fields.Date(
        string='Fecha Retiro',
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Retiro''',
    )
    state = fields.Selection(
        string='Estado',
        required=True,
        track_visibility='onchange',
        help='''Estado''',
        selection=[
            ('definido', 'definido'),
            ('revisado', 'revisado'),
            ('publicado', 'publicado'),
            ('actualizado', 'actualizado'),
            ('cancelado', 'cancelado'),
        ],
        default='definido',
    )
    acceso_id = fields.Many2one(
        string="Acceso",
        required=True,
        track_visibility='onchage',
        comodel_name='activo_informacion.acceso',
        ondelete='restrict',
        help='''Acceso''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )

    # -------------------
    # methods
    # -------------------

    @api.onchange('proceso_id')
    def _onchange_get_areas_lideres(self):
        areas_lideres = list(set([i.id for i in self.proceso_id.dependencia_lider_ids]))
        areas_gestoras = list(set([i.id for i in self.proceso_id.dependencia_gestor_ids]))
        return {
            'domain':{
                'custodio_dependencia_id': [('id','in', areas_gestoras)],
                'propietario_dependencia_id': [('id','in', areas_lideres)],
            }
        }

    @api.one
    @api.constrains('confidencialidad', 'integridad', 'disponibilidad')
    @api.onchange('confidencialidad', 'integridad', 'disponibilidad')
    def _onchage_get_criticidad(self):
        if self.confidencialidad and self.integridad and self.disponibilidad:
            data = self.env['activo_informacion.clasificacion'].search(
                  [
                      ('confidencialidad', '=', self.confidencialidad),
                      ('integridad', '=', self.integridad),
                      ('disponibilidad', '=', self.disponibilidad),
                  ],
                  limit=1,
            )
            self.criticidad = data.state
        else:
            self.criticidad = ''

    @api.one
    @api.constrains('company_location_piso')
    @api.onchange('company_location_piso')
    def _check_company_location_piso(self):
        if self.company_location_piso > 99:
            raise ValidationError("El maximo valor para piso es de  99")

class activo_informacion_clasificacion(models.Model):
    _name = 'activo_informacion.clasificacion'
    _description = 'Clasificación'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    confidencialidad = fields.Selection(
        string='Confidencialidad',
        required=True,
        track_visibility='onchange',
        help='''Confidencialidad''',
        selection=[
            ('IPR', 'ALTA'),
            ('IPC', 'MEDIA'),
            ('IPB', 'BAJA'),
        ],
    )
    integridad = fields.Selection(
        string='Integridad',
        required=True,
        track_visibility='onchange',
        help='''Integridad''',
        selection=[
            ('A', 'ALTA'),
            ('M', 'MEDIA'),
            ('B', 'BAJA'),
        ],
    )
    disponibilidad = fields.Selection(
        string='Disponibilidad',
        required=True,
        track_visibility='onchange',
        help='''Disponibilidad''',
        selection=[
            ('1', 'ALTA'),
            ('2', 'MEDIA'),
            ('3', 'BAJA'),
        ],
    )
    state = fields.Selection(
        string='Estado',
        required=True,
        track_visibility='onchange',
        help='''Estado''',
        selection=[
            ('ALTA', 'ALTA'),
            ('MEDIA', 'MEDIA'),
            ('BAJA', 'BAJA'),
        ],
    )
    activo_sistema = fields.Boolean(
        string='Habilitado en el sistema',
        required=False,
        track_visibility='onchange',
        help='''Habilitado en el sistema''',
        default=True,
    )

    # -------------------
    # methods
    # -------------------

class activo_informacion_acceso(models.Model):
    _name = 'activo_informacion.acceso'
    _description = 'Acceso'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    name = fields.Char(
        string='Nombre',
        required=True,
        track_visibility='onchange',
        size=255,
        help='''Nombre''',
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción''',
    )
    activo_sistema = fields.Boolean(
        string='Habilitado en el sistema',
        required=False,
        track_visibility='onchange',
        help='''Habilitado en el sistema''',
        default=True,
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------

