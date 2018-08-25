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


class mapa_procesos_proceso(models.Model):
    _name = 'mapa_procesos.proceso'
    _description = 'Procesos'
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
    objetivo = fields.Text(
        string='Objetivo',
        required=True,
        track_visibility='onchange',
        help='''Objetivo''',
    )
    alcance = fields.Text(
        string='Alcance',
        required=True,
        track_visibility='onchange',
        help='''Alcance''',
    )
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Tipo''',
        selection=[
            ('estrategico', 'Estratégico'),
            ('misional', 'Misional'),
            ('apoyo', 'Apoyo'),
            ('control', 'Control'),
        ],
    )
    dependencia_lider = fields.Many2one(
        string='Dependencia Lider',
        required=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Dependencia Lider''',
    )
    dependencia_gestor = fields.Many2many(
        string='Dependencia Gestor(es)',
        required=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Dependencia Gestor(es)''',
    )
    actividad_ids = fields.One2many(
        string='Actividades',
        required=False,
        track_visibility='onchange',
        comodel_name='mapa_procesos.actividad',
        inverse_name='proceso_id',
        ondelete='restrict',
        help='''Actividades''',
    )

    # -------------------
    # methods
    # -------------------

class mapa_procesos_actividad(models.Model):
    _name = 'mapa_procesos.actividad'
    _description = 'Actividad'
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
    ciclo = fields.Selection(
        string='Ciclo',
        required=True,
        track_visibility='onchange',
        help='''Ciclo PHVA''',
        selection=[
            ('planear', 'Planear'),
            ('hacer', 'Hacer'),
            ('verificar', 'Verificar'),
            ('actuar', 'Actuar'),
        ],
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción de Actividad''',
    )
    proceso_id = fields.Many2one(
        string='Proceso',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_procesos.proceso',
        ondelete='restrict',
        help='''Proceso''',
        default=lambda self: self._context.get('proceso_id', None),
    )
    entrada_ids = fields.One2many(
        string='Entradas',
        required=False,
        track_visibility='onchange',
        comodel_name='mapa_procesos.actividad_entranda',
        inverse_name='actividad_id',
        ondelete='restrict',
        help='''Entradas''',
    )
    salida_ids = fields.One2many(
        string='Salidas',
        required=False,
        track_visibility='onchange',
        comodel_name='mapa_procesos.actividad_salida',
        inverse_name='actividad_id',
        ondelete='restrict',
        help='''Salidas''',
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------

class mapa_procesos_actividad_entranda(models.Model):
    _name = 'mapa_procesos.actividad_entranda'
    _description = 'Actividad Entrada'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    name = fields.Char(
        string='Nombre',
        required=True,
        track_visibility='onchange',
        size=255,
        help='''Nombre Insumo''',
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción Insumo''',
    )
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Insumo Interno/Externo''',
        selection=[
            ('interno', 'interno'),
            ('externo', 'externo'),
        ],
    )
    proceso_ids = fields.Many2many(
        string='Procesos',
        required=False,
        track_visibility='onchange',
        comodel_name='mapa_procesos.proceso',
        ondelete='restrict',
        help='''Insumo Interno''',
    )
    proveedor_ids = fields.Many2many(
        string='Proveedor',
        required=False,
        track_visibility='onchange',
        comodel_name='res.partner',
        ondelete='restrict',
        help='''Insumo Externo''',
    )
    actividad_id = fields.Many2one(
        string='Actividad',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_procesos.actividad',
        ondelete='restrict',
        help='''Actividad''',
        default=lambda self: self._context.get('actividad_id', self.env['mapa_procesos.actividad'].browse()),
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------

class mapa_procesos_actividad_salida(models.Model):
    _name = 'mapa_procesos.actividad_salida'
    _description = 'Actividad Salida'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    name = fields.Char(
        string='Nombre',
        required=True,
        track_visibility='onchange',
        size=255,
        help='''Nombre del Producto''',
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción del Producto''',
    )
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Producto Interno/Externo''',
        selection=[
            ('interno', 'interno'),
            ('externo', 'externo'),
        ],
    )
    proceso_ids = fields.Many2many(
        string='Procesos',
        required=False,
        track_visibility='onchange',
        comodel_name='mapa_procesos.proceso',
        ondelete='restrict',
        help='''Producto Interno''',
    )
    cliente_ids = fields.Many2many(
        string='Cliente/Usuario',
        required=False,
        track_visibility='onchange',
        comodel_name='res.partner',
        ondelete='restrict',
        help='''Producto Externo''',
    )
    actividad_id = fields.Many2one(
        string='Actividad',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_procesos.actividad',
        ondelete='restrict',
        help='''Actividad''',
        default=lambda self: self._context.get('actividad_id', self.env['mapa_procesos.actividad'].browse()),
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------
