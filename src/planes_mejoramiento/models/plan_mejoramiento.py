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


TIPO_PLAN = [
    ('interno', 'Interno'),
    ('contraloria_bog', 'Contraloría de Bogotá'),
    ('contraloria_gral', 'Contraloría General'),
]

class plan_mejoramiento_tipo_calificacion(models.Model):
    _name = 'plan_mejoramiento.tipo_calificacion'
    _description = 'Tipo Calificación'
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
    activo_sistema = fields.Boolean(
        string='Habilitado en el sistema',
        required=False,
        track_visibility='onchange',
        help='''Habilitado en el sistema''',
        default=True,
    )
    tipo = fields.Selection(
        TIPO_PLAN,
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Topo''',
    )
    state = fields.Selection(
        string='Estado',
        required=True,
        track_visibility='onchange',
        help='''Estado''',
        selection=[
            ('sin_iniciar', 'Sin Iniciar'),
            ('en_progreso', 'En Progreso'),
            ('bloqueado', 'Bloqueado'),
            ('terminado', 'Terminado'),
            ('terminado_con_retraso', 'Terminado Con Retraso'),
        ],
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------

class plan_mejoramiento_recurso(models.Model):
    _name = 'plan_mejoramiento.recurso'
    _description = 'Recurso'
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
    tipo = fields.Selection(
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Topo''',
        selection=[
            ('financiero', 'Financiero'),
            ('humano', 'Humano'),
            ('tecnologico', 'Tecnologico'),
            ('fisico', 'Fisico'),
        ],
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Este name ya está registrado'),
    ]

    # -------------------
    # methods
    # -------------------

class plan_mejoramiento_causa(models.Model):
    _name = 'plan_mejoramiento.causa'
    _description = 'Causa'
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

class plan_mejoramiento_origen(models.Model):
    _name = 'plan_mejoramiento.origen'
    _description = 'Origen Plan de Mejoramiento'
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
    parent_id = fields.Many2one(
        string='Padre',
        required=False,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.origen',
        ondelete='restrict',
        help='''Padre''',
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

class plan_mejoramiento_plan(models.Model):
    _name = 'plan_mejoramiento.plan'
    _description = 'Plan Mejoramiento'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']
    _inherits = {
        'project.project': 'project_id',
    }

    # -------------------
    # Fields
    # -------------------
    tipo = fields.Selection(
        TIPO_PLAN,
        string='Tipo',
        required=True,
        track_visibility='onchange',
        help='''Topo''',
    )
    project_id = fields.Many2one(
        string='Proyecto',
        required=True,
        comodel_name='project.project',
        ondelete='restrict',
        help='''Proyecto''',
    )
    radicado = fields.Char(
        string='Radicado',
        required=False,
        track_visibility='onchange',
        help='''Radicado''',
    )
    dependencia_id = fields.Many2one(
        string='Unidad',
        required=False,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad''',
        readonly=True,
        default=lambda self: self.env.user.department_id.id,
    )
    origen_id = fields.Many2one(
        string='Origen',
        required=False,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.origen',
        ondelete='restrict',
        help='''Origen''',
        domain="[('parent_id','=',False)]",
    )
    sub_origen_id = fields.Many2one(
        string='Sub Origen',
        required=False,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.origen',
        ondelete='restrict',
        help='''Sub Origne''',
        domain="[('parent_id','=',origen_id)]",
    )
    facha = fields.Date(
        string='Fecha Registro',
        required=False,
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Registro''',
        default=fields.Date.today,
    )
    hallazgo_ids = fields.Text(
        string='Hallazgos',
        required=False,
        help='''Hallazgos''',
    )

    # -------------------
    # methods
    # -------------------

    @api.model
    def create(self, vals):
        plan = super(plan_mejoramiento_plan, self).create(vals)
        plan.project_id.write({
            'proyecto_tipo': 'plan_mejoramiento',
            'active': False, # El registro no se elimina, solo que no es visible en el listado de project.project,
                             # por el momento no es necesario que la gente acceda a este project.project
                             # si se requiere solo se desarchiva el registro y se gestiona comun y corriente.
        })
        plan.project_id.edt_raiz_id = self.env['project.edt'].create({
          'name': plan.project_id.name,
          'user_id': plan.project_id.user_id.id,
        })
        return plan

    @api.one
    def write(self, vals):
        res = super(plan_mejoramiento_plan, self).write(vals)
        if vals.get('user_id', False):
            self.project_id.edt_raiz_id.write({
                'user_id': vals.get('user_id'),
            })
        return res


class plan_mejoramiento_hallazgo(models.Model):
    _name = 'plan_mejoramiento.hallazgo'
    _description = 'Hallazgo'
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
    user_id = fields.Many2one(
        string='Auditor',
        required=True,
        track_visibility='onchange',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Auditro''',
        default=lambda self: self._context.get('uid', self.env['res.users'].browse()),
    )
    causa_ids = fields.Many2many(
        string='Causas',
        required=False,
        comodel_name='plan_mejoramiento.causa',
        ondelete='restrict',
        help='''Causas''',
    )
    proceso_id = fields.Many2one(
        string='Proceso',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_procesos.proceso',
        ondelete='restrict',
        help='''Proceso''',
    )
    dependencia_id = fields.Many2one(
        string='Unidad',
        required=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad''',
    )
    fecha_inicio = fields.Date(
        string='Fecha Inicio',
        required=False,
        readonly=True,
        track_visibility='onchange',
        compute='_compute_fecha_inicio',
        help='''Comprendida entre la fecha menor de sus Acciones''',
    )
    fecha_fin = fields.Date(
        string='Fecha Fin',
        required=False,
        readonly=True,
        track_visibility='onchange',
        compute='_compute_fecha_fin',
        help='''Comprendida entre la fecha mayor de sus Acciones''',
    )
    state = fields.Selection(
        string='Estado',
        required=False,
        track_visibility='onchange',
        help='''Estado''',
        selection=[
            ('en_progreso', 'en_progreso'),
            ('terminado', 'terminado'),
            ('cancelado', 'cancelado'),
        ],
        default='en_progreso',
    )
    plan_id = fields.Many2one(
        string='Plan de Mejoramiento',
        required=True,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.plan',
        ondelete='restrict',
        help='''Plan de Mejoramiento''',
        default=lambda self: self._context.get('plan_id', self.env['plan_mejoramiento.plan'].browse()),
    )
    plan_tipo = fields.Selection(
        string='Tipo Plan de Mejoramiento',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='plan_id.tipo',
        help='''Tipo Plan de Mejoramiento''',
    )
    acciones_ids = fields.Text(
        string='Acciones',
        required=False,
        help='''Acciones''',
    )

    # -------------------
    # methods
    # -------------------

    @api.one
    def _compute_fecha_inicio(self):
        self.fecha_inicio = "1994-07-05"

    @api.one
    def _compute_fecha_fin(self):
        self.fecha_fin = "1990-04-22"

class plan_mejoramiento_accion(models.Model):
    _name = 'plan_mejoramiento.accion'
    _description = 'Hallazgo'
    _inherit = ['mail.thread', 'models.soft_delete.mixin', 'models.fields.security.mixin']

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
        required=False,
        track_visibility='onchange',
        help='''Topo''',
        selection=[
            ('preventivo', 'preventivo'),
            ('correctivo', 'correctivo'),
            ('mejoramiento', 'mejoramiento'),
            ('correccion', 'correccion'),
        ],
    )
    state = fields.Selection(
        string='Estado',
        required=False,
        track_visibility='onchange',
        help='''Estado''',
        selection=[
            ('nuevo', 'nuevo'),
            ('por_aprobar', 'por_aprobar'),
            ('en_progreso', 'en_progreso'),
            ('terminado', 'terminado'),
            ('cancelado', 'cancelado'),
        ],
        default='en_progreso',
    )
    ejecutor_id = fields.Many2one(
        string='Ejecutor',
        required=True,
        readonly=True,
        track_visibility='onchange',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Ejecutor''',
        default=lambda self: self._context.get('uid', self.env['res.users'].browse()),
    )
    dependencia_id = fields.Many2one(
        string='Unidad',
        required=False,
        readonly=True,
        track_visibility='onchange',
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad''',
    )
    jefe_dependencia_id = fields.Many2one(
        string='Jefe Dependencia',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='dependencia_id.manager_id.user_id',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Jefe Dependencia''',
    )
    user_id = fields.Many2one(
        string='Auditor',
        required=True,
        readonly=True,
        track_visibility='onchange',
        related='hallazgo_id.user_id',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Auditro''',
    )
    objetivo = fields.Char(
        string='Objetivo',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Objetivo''',
    )
    indicador = fields.Char(
        string='Indicador',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Indicador''',
    )
    unidad_medida = fields.Char(
        string='Unidad de Medida',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Unidad de Medida''',
    )
    meta = fields.Char(
        string='Meta',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Meta''',
    )
    recurso_ids = fields.Many2many(
        string='Recursos',
        required=False,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.recurso',
        ondelete='restrict',
        help='''Recursos''',
    )
    facha_inicio = fields.Date(
        string='Fecha Inicio',
        required=False,
        track_visibility='onchange',
        help='''Fecha Inicio''',
    )
    facha_fin = fields.Date(
        string='Fecha Fin',
        required=False,
        track_visibility='onchange',
        help='''Fecha Fin''',
    )
    facha_creacion = fields.Date(
        string='Fecha Registro',
        required=False,
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Registro''',
        default=fields.Date.today,
    )
    hallazgo_id = fields.Many2one(
        string='Hallazgo',
        required=True,
        comodel_name='plan_mejoramiento.hallazgo',
        ondelete='restrict',
        help='''Hallazgo''',
        default=lambda self: self._context.get('hallazgo_id', self.env['plan_mejoramiento.hallazgo'].browse()),
    )
    hallazgo_dependencia_id = fields.Many2one(
        string='Unidad Del Hallazgo',
        required=False,
        readonly=True,
        related='hallazgo_id.dependencia_id',
        ondelete='restrict',
        help='''Unidad Del Hallazgo''',
    )
    plan_tipo = fields.Selection(
        required=False,
        readonly=True,
        related='hallazgo_id.plan_tipo',
    )
    plan_id = fields.Many2one(
        required=False,
        readonly=True,
        related='hallazgo_id.plan_id',
        comodel_name='plan_mejoramiento.plan',
        ondelete='restrict',
    )
    task_ids = fields.Text(
        string='Tareas',
        required=False,
        track_visibility='onchange',
        help='''Tareas''',
    )
    avance_ids = fields.Text(
        string='Avances',
        required=False,
        help='''Avances''',
    )

    # -------------------
    # methods
    # -------------------

class plan_mejoramiento_avance(models.Model):
    _name = 'plan_mejoramiento.avance'
    _description = 'Avances'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']

    # -------------------
    # Fields
    # -------------------
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción''',
    )
    facha_creacion = fields.Date(
        string='Fecha Registro',
        required=False,
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Registro''',
        default=fields.Date.today,
    )
    aprobacion_jefe_dependencia = fields.Boolean(
        string='Aprobación Jefe Unidad',
        required=False,
        track_visibility='onchange',
        help='''Aprobación Jefe Unidad''',
        default=False,
    )
    tipo_calificacion_id = fields.Many2one(
        string='Tipo Calificación',
        required=False,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.tipo_calificacion',
        ondelete='restrict',
        help='''Tipo Calificación''',
        domain="[('tipo','=',plan_tipo)]",
    )
    state = fields.Selection(
        string='Estado',
        required=False,
        track_visibility='onchange',
        related='tipo_calificacion_id.state',
        help='''Estado''',
    )
    porcentaje_avance = fields.Text(
        string='% de Avance',
        required=False,
        track_visibility='onchange',
        help='''% de Avance Calificado''',
    )
    observacion = fields.Text(
        string='Observaciones',
        required=False,
        track_visibility='onchange',
        help='''Observaciones''',
    )
    accion_id = fields.Many2one(
        string='Actividad',
        required=True,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.accion',
        ondelete='restrict',
        help='''Actividad''',
        domain="[('state','=','en_progreso')]",
        default=lambda self: self._context.get('accion_id', self.env['plan_mejoramiento.accion'].browse()),
    )
    dependencia_id = fields.Many2one(
        string='Unidad',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='accion_id.dependencia_id',
        ondelete='restrict',
        help='''Unidad''',
    )
    accion_descripcion = fields.Text(
        string='Descripción Acción',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='accion_id.descripcion',
        help='''Descripción Acción''',
    )
    plan_tipo = fields.Selection(
        string='Tipo Plan de Mejoramiento',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='accion_id.plan_tipo',
        help='''Tipo Plan de Mejoramiento''',
    )
    jefe_dependencia_id = fields.Many2one(
        string='Jefe Dependencia',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='accion_id.jefe_dependencia_id',
        ondelete='restrict',
        help='''Jefe Dependencia''',
    )
    ejecutor_id = fields.Many2one(
        string='Ejecutor',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='accion_id.ejecutor_id',
        ondelete='restrict',
        help='''Ejecutor''',
    )

    # -------------------
    # methods
    # -------------------
