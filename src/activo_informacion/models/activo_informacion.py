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
    propietario = fields.Text(
        string='Propietario',
        required=True,
        track_visibility='onchange',
        help='''Propietario''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
    )
    custodio = fields.Text(
        string='Custodio',
        required=True,
        track_visibility='onchange',
        help='''Custodio''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
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
    ubicacion = fields.Text(
        string='Ubicación',
        required=True,
        track_visibility='onchange',
        help='''Ubicación''',
        readonly=True,
        states={
            'definido': [('readonly', False)],
            'actualizado': [('readonly', False)],
        }
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
        track_visibility='onchange',
        size=255,
        compute='_compute_criticidad',
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

    # -------------------
    # methods
    # -------------------

    @api.one
    def _compute_criticidad(self):
        self.criticidad = "Adult hundred TV participant course."
