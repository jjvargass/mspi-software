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


class activo_informacion_activo_tipo(models.Model):
    _name = 'activo_informacion.activo_tipo'
    _description = 'Tipo Activo de Información'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    active = fields.Boolean(
        string='Habilitado en el sistema',
        required=True,
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
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Tipo''',
        selection=[
            ('informacion', 'informacion'),
            ('software', 'software'),
            ('resursoh', 'resursoh'),
            ('servicio', 'servicio'),
            ('hardware', 'hardware'),
            ('otros', 'otros'),
        ],
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
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción''',
    )
    proceso_id = fields.Many2one(
        string='Proceso',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_procesos.proceso',
        ondelete='restrict',
        help='''Proceso''',
    )
    propietario = fields.Text(
        string='Propietario',
        required=True,
        track_visibility='onchange',
        help='''Propietario''',
    )
    custodio = fields.Text(
        string='Custodio',
        required=True,
        track_visibility='onchange',
        help='''Custodio''',
    )
    tipo_para_busqueda = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        store=False,
        help='''Tipo''',
        selection=[
            ('informacion', 'informacion'),
            ('software', 'software'),
            ('resursoh', 'resursoh'),
            ('servicio', 'servicio'),
            ('hardware', 'hardware'),
            ('otros', 'otros'),
        ],
    )
    tipo = fields.Many2one(
        string='Detalle Tipo',
        required=True,
        track_visibility='onchange',
        comodel_name='activo_informacion.activo_tipo',
        ondelete='restrict',
        help='''Detalle Tipo''',
    )
    ubicacion = fields.Text(
        string='Ubicación',
        required=True,
        track_visibility='onchange',
        help='''Ubicación''',
    )
    confidencialidad = fields.Selection(
        string='Confidencialidad',
        required=True,
        track_visibility='onchange',
        help='''Confidencialidad''',
        selection=[
            ('ipr', 'IPR'),
            ('ipc', 'IPC'),
            ('ipb', 'IPB'),
        ],
    )
    confidencialidad_justificacion = fields.Text(
        string='Justificación Confidencialidad',
        required=True,
        track_visibility='onchange',
        help='''describe el impacto que causaría la pérdida de la confidencialidad''',
    )
    integridad = fields.Selection(
        string='Integridad',
        required=True,
        track_visibility='onchange',
        help='''Integridad''',
        selection=[
            ('a', 'A'),
            ('m', 'M'),
            ('b', 'B'),
        ],
    )
    integridad_justificacion = fields.Text(
        string='Justificación Integridad',
        required=True,
        track_visibility='onchange',
        help='''describe el impacto que causaría la pérdida de la Integridad''',
    )
    disponibilidad = fields.Selection(
        string='Disponibilidad',
        required=True,
        track_visibility='onchange',
        help='''Disponibilidad''',
        selection=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        ],
    )
    disponibilidad_justicicacion = fields.Text(
        string='Justificación Disponibilidad',
        required=True,
        track_visibility='onchange',
        help='''describe el impacto que causaría la pérdida de la disponibilidad''',
    )
    criticidad = fields.Char(
        string='Criticidad',
        required=True,
        track_visibility='onchange',
        size=255,
        compute='_compute_criticidad',
        help='''Valor general del Activo''',
    )
    fecha_ingreso = fields.Date(
        string='Fecha Ingreso',
        required=True,
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Ingreso''',
    )
    fecha_retiro = fields.Date(
        string='Fecha Retiro',
        required=True,
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
            ('edicion', 'edicion'),
            ('por_aprobar', 'por_aprobar'),
            ('ingresado', 'ingresado'),
            ('retirado', 'retirado'),
        ],
        default='edicion',
    )

    # -------------------
    # methods
    # -------------------

    @api.one
    def _compute_criticidad(self):
        self.criticidad = "Adult hundred TV participant course."
