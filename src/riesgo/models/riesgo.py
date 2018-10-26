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


class riesgo_factor(models.Model):
    _name = 'riesgo.factor'
    _description = 'Tipo Contexto'
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
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Topo''',
        selection=[
            ('interno', 'interno'),
            ('externo', 'externo'),
        ],
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

class riesgo_contexto(models.Model):
    _name = 'riesgo.contexto'
    _description = 'Contexto'
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
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Topo''',
        selection=[
            ('interno', 'interno'),
            ('externo', 'externo'),
        ],
    )
    factor_id = fields.Many2one(
        string='Factor',
        required=True,
        track_visibility='onchange',
        comodel_name='riesgo.factor',
        ondelete='restrict',
        help='''Factor''',
        domain="[('tipo','=',tipo), ('activo_sistema','=',True)]",
    )

    # -------------------
    # methods
    # -------------------

class riesgo_causa(models.Model):
    _name = 'riesgo.causa'
    _description = 'Causa'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    que = fields.Text(
        string='¿Qué Puede Suceder?',
        required=True,
        track_visibility='onchange',
        help='''¿Qué Puede Suceder?''',
    )
    como = fields.Text(
        string='¿Como Puede Suceder?',
        required=True,
        track_visibility='onchange',
        help='''¿Como Puede Suceder?''',
    )
    cuando = fields.Text(
        string='¿Cuándo Puede Suceder?',
        required=True,
        track_visibility='onchange',
        help='''¿Cuándo Puede Suceder?''',
    )
    consecuencia = fields.Text(
        string='¿Que Consecuencia Tendria su Materialización?',
        required=True,
        track_visibility='onchange',
        help='''¿Que Consecuencia Tendria su Materialización?''',
    )

    # -------------------
    # methods
    # -------------------

class riesgo_tipo_riesgo(models.Model):
    _name = 'riesgo.tipo_riesgo'
    _description = 'Tipo Riesgo'
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

class riesgo_probabilidad(models.Model):
    _name = 'riesgo.probabilidad'
    _description = 'Probabilidad'
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
    nivel = fields.Integer(
        string='Nivel',
        required=True,
        track_visibility='onchange',
        help='''Nivel''',
    )
    frecuencia = fields.Text(
        string='Frecuencia',
        required=True,
        track_visibility='onchange',
        help='''Frecuencia''',
    )
    activo_sistema = fields.Boolean(
        string='Habilitado en el sistema',
        required=False,
        track_visibility='onchange',
        help='''Habilitado en el sistema''',
        default=True,
    )

    _sql_constraints = [
        ('unique_nivel', 'unique(nivel)', 'Este nivel ya está registrado'),
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------

class riesgo_impacto(models.Model):
    _name = 'riesgo.impacto'
    _description = 'Impacto'
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
    nivel = fields.Integer(
        string='Nivel',
        required=True,
        track_visibility='onchange',
        help='''Nivel''',
    )
    cuantitativo = fields.Text(
        string='Impacto Cuantitativo',
        required=True,
        track_visibility='onchange',
        help='''Impacto Cuantitativo''',
    )
    cualitativo = fields.Text(
        string='Impacto Cualitativo',
        required=True,
        track_visibility='onchange',
        help='''Impacto Cualitativo''',
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

class riesgo_control(models.Model):
    _name = 'riesgo.control'
    _description = 'Control'
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
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Tipo''',
        selection=[
            ('preventivo', 'preventivo'),
            ('correctivo', 'correctivo'),
        ],
    )
    implementacion = fields.Selection(
        string='Implementación',
        required=True,
        track_visibility='onchange',
        help='''Implementación''',
        selection=[
            ('automatico', 'automatico'),
            ('manual', 'manual'),
        ],
    )
    documentado = fields.Boolean(
        string='¿Documentado?',
        required=True,
        track_visibility='onchange',
        help='''¿Documentado?''',
    )
    responsables_ids = fields.Many2many(
        string='Responsables',
        required=False,
        track_visibility='onchange',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Responsables''',
    )
    periodicidad = fields.Selection(
        string='Periodicidad',
        required=True,
        track_visibility='onchange',
        help='''Periodicidad''',
        selection=[
            ('diario', 'diario'),
            ('quincenal', 'quincenal'),
            ('mensual', 'mensual'),
            ('trimestral', 'trimestral'),
            ('semestral', 'semestral'),
            ('anual', 'anual'),
        ],
    )

    # -------------------
    # methods
    # -------------------

class riesgo_riesgo(models.Model):
    _name = 'riesgo.riesgo'
    _description = 'Riesgo'
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
        comodel_name='mapa_proceso.proceso',
        ondelete='restrict',
        help='''Proceso''',
    )
    seguridad_de_la_informacion = fields.Boolean(
        string='¿En seguridad de la información?',
        required=False,
        track_visibility='onchange',
        help='''¿En seguridad de la información?''',
        default=True,
    )
    activo_informacion_id = fields.Many2one(
        string='Activo de Información',
        required=False,
        track_visibility='onchange',
        comodel_name='activo_informacion.activo',
        ondelete='restrict',
        help='''Activo de Información''',
    )
    causa_ids = fields.Many2many(
        string='Causas',
        required=False,
        comodel_name='riesgo.causa',
        ondelete='restrict',
        help='''Causas''',
    )
    contexto_ids = fields.Many2many(
        string='Contexto',
        required=False,
        comodel_name='riesgo.contexto',
        ondelete='restrict',
        help='''Contexto''',
    )
    tipo_riesgo_id = fields.Many2one(
        string='Tipo Riesgo',
        required=True,
        track_visibility='onchange',
        comodel_name='riesgo.tipo_riesgo',
        ondelete='restrict',
        help='''Tipo Riesgo''',
    )
    probabilidad_id = fields.Many2one(
        string='Probabilida',
        required=True,
        track_visibility='onchange',
        comodel_name='riesgo.probabilidad',
        ondelete='restrict',
        help='''Probabilidad''',
    )
    user_id = fields.Many2one(
        string='Registrador',
        required=True,
        readonly=True,
        track_visibility='onchange',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Registrador''',
        default=lambda self: self._context.get('uid', self.env['res.users'].browse()),
    )
    dependencia_id = fields.Many2one(
        string='Unidad',
        required=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad''',
    )
    impacto_id = fields.Many2one(
        string='Impacto',
        required=True,
        track_visibility='onchange',
        comodel_name='riesgo.impacto',
        ondelete='restrict',
        help='''Impacto''',
    )
    evaluar_control_ids = fields.Text(
        string='Evaluar Control',
        required=False,
        help='''Evaluar Control''',
    )

    # -------------------
    # methods
    # -------------------

class riesgo_evaluacion_control(models.Model):
    _name = 'riesgo.evaluacion_control'
    _description = 'Evaluar Control'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    name = fields.Char(
        string='Nombre',
        required=True,
        size=255,
        help='''Nombre''',
    )
    riesgo_id = fields.Many2one(
        string='Riesgo',
        required=True,
        track_visibility='onchange',
        comodel_name='riesgo.riesgo',
        ondelete='restrict',
        help='''Riesgo''',
    )
    control_id = fields.Many2one(
        string='Control',
        required=True,
        track_visibility='onchange',
        comodel_name='riesgo.control',
        ondelete='restrict',
        help='''Control''',
    )
    existe_documentacion = fields.Boolean(
        string='¿Existen Documentación?',
        required=True,
        track_visibility='onchange',
        help='''¿Existen manuales, instructivos o procedimientos para el
manejo del control?''',
        default=True,
    )
    existe_responsable = fields.Boolean(
        string='¿Existen Responsables?',
        required=False,
        help='''¿Está(n) definido(s) el(los) responsable(s) de la ejecución del
control y del seguimiento?''',
        default=True,
    )
    es_automatico = fields.Boolean(
        string='¿El control es automático?',
        required=False,
        help='''¿El control es automático?''',
        default=True,
    )
    es_manual = fields.Boolean(
        string='¿El control es manual?',
        required=False,
        help='''¿El control es manual?''',
        default=True,
    )
    frecuencia_adecuada = fields.Boolean(
        string='¿Frecuencia Adecuada?',
        required=False,
        help='''¿La frecuencia de ejecución del control y seguimiento es
adecuada?''',
        default=True,
    )
    existe_evidencia = fields.Boolean(
        string='¿Existe Evidencias de la Ejecución?',
        required=False,
        help='''¿Se cuenta con evidencias de la ejecución y seguimiento del
control?''',
        default=True,
    )
    es_efectiva = fields.Boolean(
        string='¿Es Efectivo?',
        required=False,
        help='''¿En el tiempo que lleva la herramienta ha demostrado ser
efectiva?''',
        default=True,
    )

    _sql_constraints = [
        ('unique_riesgo_id', 'unique(riesgo_id)', 'Este riesgo_id ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------
