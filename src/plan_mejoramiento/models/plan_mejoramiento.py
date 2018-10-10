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
from openerp.exceptions import  Warning, AccessError, ValidationError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openid import store


TIPO_PLAN = [
    ('interno', 'Interno'),
    ('contraloria_bog', 'Contraloría de Bogotá'),
    ('contraloria_gral', 'Contraloría General'),
]

class plan_mejoramiento_parametro_activar_avance(models.Model):
    _name = 'plan_mejoramiento.parametro_activar_avance'
    _description = 'Parametro Activar Avance'
    _inherit = ['mail.thread', 'models.soft_delete.mixin']
    # -------------------
    # Fields
    # -------------------
    fecha_inicio = fields.Date(
        string='Fecha Inicio',
        required=True,
        help='''Fecha inicio para registra avances''',
    )
    fecha_fin = fields.Date(
        string='Fecha Fin',
        required=True,
        help='''Fecha fin para registrar avances''',
    )
    facha_creacion = fields.Date(
        string='Fecha Registro',
        required=True,
        readonly=True,
        help='''Fecha Registro''',
        default=fields.Date.today,
    )

    # -------------------
    # methods
    # -------------------

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
        help='''Tipo''',
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
    fecha = fields.Date(
        string='Fecha Registro',
        required=False,
        readonly=True,
        track_visibility='onchange',
        help='''Fecha Registro''',
        default=fields.Date.today,
    )
    hallazgo_ids = fields.One2many(
        string='Hallazgos',
        required=False,
        help='''Hallazgos''',
        comodel_name='plan_mejoramiento.hallazgo',
        inverse_name='plan_id',
        ondelete='restrict',
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

    @api.multi
    def hallazgo_view_button(self):
        return {
            'name': 'Hallazgos',
            'res_model': 'plan_mejoramiento.hallazgo',
            'domain': [('plan_id', '=', self.id)],
            'context': {'plan_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'form',
        }

    @api.multi
    def accion_view_button(self):
        return {
            'name': 'Acciones',
            'res_model': 'plan_mejoramiento.accion',
            'domain': [('plan_id', '=', self.id)],
            'context': {'plan_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'form',
        }

    @api.multi
    def avance_view_button(self):
        return {
            'name': 'Avances',
            'res_model': 'plan_mejoramiento.avance',
            'domain': [('plan_id', '=', self.id)],
            'context': {'plan_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'form',
        }

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
        readonly=True,
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
        domain="[('activo_sistema','=',True)]",
    )
    proceso_id = fields.Many2one(
        string='Proceso',
        required=True,
        track_visibility='onchange',
        comodel_name='mapa_proceso.proceso',
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
            ('en_progreso', 'En Progreso'),
            ('terminado', 'Terminado'),
            ('cancelado', 'Cancelado'),
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
        store=True,
        track_visibility='onchange',
        related='plan_id.tipo',
        help='''Tipo Plan de Mejoramiento''',
    )
    accion_ids = fields.One2many(
        string='Acciones',
        required=False,
        help='''Acciones''',
        comodel_name='plan_mejoramiento.accion',
        inverse_name='hallazgo_id',
        ondelete='restrict',
    )

    # -------------------
    # methods
    # -------------------

    @api.onchange('proceso_id')
    def _onchange_proceso_id(self):
        lideres = self.proceso_id.dependencia_lider
        print lideres
        gestores = self.proceso_id.dependencia_gestor_ids
        all_areas = lideres + gestores
        print all_areas

    @api.one
    def _compute_fecha_inicio(self):
        for hallazgo in self:
            self.env.cr.execute("""
                        SELECT
                            MIN(fecha_inicio)
                        FROM
                            plan_mejoramiento_accion t
                        WHERE
                            t.hallazgo_id = %s
                     """, (hallazgo.id,))
        date_min = self.env.cr.fetchall()[0][0]
        self.fecha_inicio = date_min

    @api.one
    def _compute_fecha_fin(self):
        for hallazgo in self:
            self.env.cr.execute("""
                        SELECT
                            MAX(fecha_fin)
                        FROM
                            plan_mejoramiento_accion t
                        WHERE
                            t.hallazgo_id = %s
                     """, (hallazgo.id,))
        date_max = self.env.cr.fetchall()[0][0]
        self.fecha_fin = date_max

    @api.multi
    def accion_view_button(self):
        return {
            'name': 'Acciones',
            'res_model': 'plan_mejoramiento.accion',
            'domain': [('hallazgo_id', '=', self.id)],
            'context': {'hallazgo_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'form',
        }

    @api.multi
    def avance_view_button(self):
        return {
            'name': 'Avances',
            'res_model': 'plan_mejoramiento.avance',
            'domain': [('hallazgo_id', '=', self.id)],
            'context': {'hallazgo_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'form',
        }

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
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    descripcion = fields.Text(
        string='Descripción',
        required=True,
        track_visibility='onchange',
        help='''Descripción''',
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    tipo = fields.Selection(
        string='Tipo',
        required=False,
        track_visibility='onchange',
        help='''Topo''',
        selection=[
            ('preventivo', 'Preventivo'),
            ('correctivo', 'Correctivo'),
            ('mejoramiento', 'Mejoramiento'),
            ('correccion', 'Corrección'),
        ],
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    state = fields.Selection(
        string='Estado',
        required=False,
        track_visibility='onchange',
        help='''Estado''',
        selection=[
            ('nuevo', 'Nuevo'),
            ('por_aprobar', 'Por Aprobar'),
            ('en_progreso', 'En Progreso'),
            ('terminado', 'Terminado'),
            ('cancelado', 'Cancelado'),
        ],
        default='nuevo',
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
        default=lambda self: self.env.user.department_id.id,
    )
    jefe_dependencia_id = fields.Many2one(
        string='Jefe Unidad',
        required=True,
        readonly=True,
        track_visibility='onchange',
        related='dependencia_id.manager_id.user_id',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Jefe Unidad''',
    )
    user_id = fields.Many2one(
        string='Auditor',
        required=False,
        readonly=True,
        store=True,
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
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    indicador = fields.Char(
        string='Indicador',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Indicador''',
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    unidad_medida = fields.Char(
        string='Unidad de Medida',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Unidad de Medida''',
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    meta = fields.Char(
        string='Meta',
        required=False,
        track_visibility='onchange',
        size=255,
        help='''Meta''',
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    recurso_ids = fields.Many2many(
        string='Recursos',
        required=False,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.recurso',
        ondelete='restrict',
        help='''Recursos''',
        domain="[('activo_sistema','=',True)]",
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    fecha_inicio = fields.Date(
        string='Fecha Inicio',
        required=True,
        track_visibility='onchange',
        help='''Fecha Inicio''',
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    fecha_fin = fields.Date(
        string='Fecha Fin',
        required=True,
        track_visibility='onchange',
        help='''Fecha Fin''',
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
    )
    fecha_creacion = fields.Date(
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
        domain="[('dependencia_id', '=', dependencia_id )]",
        default=lambda self: self._context.get('hallazgo_id', self.env['plan_mejoramiento.hallazgo'].browse()),
        readonly=True,
        states={
            'nuevo': [('readonly', False)],
        }
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
        store=True,
        related='hallazgo_id.plan_tipo',
    )
    plan_id = fields.Many2one(
        required=False,
        readonly=True,
        store=True,
        related='hallazgo_id.plan_id',
        comodel_name='plan_mejoramiento.plan',
        ondelete='restrict',
    )
    task_ids = fields.One2many(
        string='Tareas',
        required=False,
        comodel_name='project.task',
        inverse_name='accion_id',
        ondelete='restrict',
    )
    avance_ids = fields.One2many(
        string='Avances',
        required=False,
        help='''Avances''',
        comodel_name='plan_mejoramiento.avance',
        inverse_name='accion_id',
        ondelete='restrict',
    )

    # -------------------
    # methods
    # -------------------
    @api.one
    @api.constrains('fecha_inicio')
    def _check_fecha_inicio(self):
        self._check_fechas()

    @api.one
    @api.constrains('fecha_fin')
    def _check_fecha_fin(self):
        self._check_fechas()
        fecha_inicio = datetime.strptime(self.fecha_inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(self.fecha_fin, '%Y-%m-%d')
        year = relativedelta(years=1)
        tope = fecha_inicio + year
        #if fecha_fin > tope:
        #    raise ValidationError('No se permite que la vigencia de una acción sea superior a un año')

    @api.one
    def _check_fechas(self):
        if(self.fecha_inicio and self.fecha_fin and
           self.fecha_inicio > self.fecha_fin
            ):
            raise ValidationError("Fecha de inicio no puede ser posterior a la de finalización")

    @api.model
    def create(self, vals):
        accion = super(plan_mejoramiento_accion, self).create(vals)
        accion.task_ids.write({'project_id': self.hallazgo_id.plan_id.project_id.id, 'edt_id': self.hallazgo_id.plan_id.project_id.edt_raiz_id.id, 'revisor_id': accion.ejecutor_id.id, 'accion_id': accion.id})
        return accion

    @api.one
    def write(self, vals):
        if ('task_ids' in vals or 'avances_ids' in vals) and self.state != 'en_progreso':
            raise ValidationError('No se permite adicionar tareas o avances en una Acción que no esta en progreso')
        result = super(plan_mejoramiento_accion, self).write(vals)
        if 'dependencia_id' in vals or 'jefe_dependencia_id' in vals or 'task_ids' in vals:
            self.task_ids.write({'project_id': self.hallazgo_id.plan_id.project_id.id, 'edt_id': self.hallazgo_id.plan_id.project_id.edt_raiz_id.id, 'revisor_id': self.ejecutor_id.id, 'accion_id': self.id})
        return result

    @api.multi
    def avance_view_button(self):
        return {
            'name': 'Avances',
            'res_model': 'plan_mejoramiento.avance',
            'domain': [('accion_id', '=', self.id)],
            'context': {'accion_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'form',
        }

    # -------------------
    # Workflow methods
    # -------------------
    def wkf_nuevo(self):
        self.state = 'nuevo'

    def wkf_cancelado(self):
        self.state = 'cancelado'

    def wkf_en_progreso(self):
        self.state = 'en_progreso'

    def wkf_por_aprobar(self):
        self.state = 'por_aprobar'

    def wkf_terminado(self):
        self.state = 'terminado'

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
    fecha_creacion = fields.Date(
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
        store=True,
        track_visibility='onchange',
        related='tipo_calificacion_id.state',
        help='''Estado''',
    )
    porcentaje_avance = fields.Integer(
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
    dependencia_user_registrador_id = fields.Many2one(
        string='Unidad Usuario Registrador',
        required=False,
        readonly=True,
        store=False,
        comodel_name='hr.department',
        ondelete='restrict',
        help='''Unidad Usuario Registrador''',
        default=lambda self: self.env.user.department_id.id,
    )

    accion_id = fields.Many2one(
        string='Acción',
        required=True,
        store=True,
        track_visibility='onchange',
        comodel_name='plan_mejoramiento.accion',
        ondelete='restrict',
        help='''Acción''',
        domain="[('state','=','en_progreso'),('dependencia_id', '=', dependencia_user_registrador_id )]",
        default=lambda self: self._context.get('accion_id', self.env['plan_mejoramiento.accion'].browse()),
    )
    dependencia_id = fields.Many2one(
        string='Unidad',
        required=False,
        readonly=True,
        store=True,
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
        store=True,
        track_visibility='onchange',
        related='accion_id.plan_tipo',
        help='''Tipo Plan de Mejoramiento''',
    )
    plan_id = fields.Many2one(
        required=False,
        readonly=True,
        store=True,
        related='accion_id.plan_id',
        comodel_name='plan_mejoramiento.plan',
        ondelete='restrict',
    )
    hallazgo_id = fields.Many2one(
        required=False,
        readonly=True,
        store=True,
        related='accion_id.hallazgo_id',
        comodel_name='plan_mejoramiento.hallazgo',
        ondelete='restrict',
    )
    jefe_dependencia_id = fields.Many2one(
        string='Jefe Unidad',
        required=False,
        readonly=True,
        track_visibility='onchange',
        related='accion_id.jefe_dependencia_id',
        ondelete='restrict',
        help='''Jefe Unidad''',
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
    user_id = fields.Many2one(
        string='Auditor',
        required=False,
        readonly=True,
        store=True,
        track_visibility='onchange',
        related='accion_id.user_id',
        comodel_name='res.users',
        ondelete='restrict',
        help='''Auditro''',
    )

    # -------------------
    # methods
    # -------------------
    @api.onchange('porcentaje_avance')
    def onchange_porcentaje_avance(self):
        if self.porcentaje_avance and (self.porcentaje_avance < 0 or self.porcentaje_avance > 100):
            return {
                'warning': {'message': 'Valor Fuera del Rango Permitido'}
            }

    @api.constrains('porcentaje_avance')
    def check_porcentaje_avance(self):
        if self.porcentaje_avance < 0 or self.porcentaje_avance > 100:
            raise Warning('No se Permite Guardar un Valor Mayor a 100 y Menor a 0 para el Porcentaje de Avance')

    @api.model
    def create(self, vals):
        hoy = fields.Date.today()
        fecha_max = self.env['plan_mejoramiento.parametro_activar_avance'].search([],
            order='create_date DESC',
            limit=1,
        )
        fecha_inicio = fecha_max.fecha_inicio
        fecha_fin = fecha_max.fecha_fin

        if not fecha_inicio or not fecha_fin:
            raise Warning('No se ha definido fechas para el registro de avances')

        if fecha_inicio and fecha_fin and not (fecha_inicio <= hoy <= fecha_fin):
            raise Warning('Aún no se ha habilitado las fechas para realizar avances')

        # Unico registro de avance en el mes
        if fecha_inicio and fecha_fin:
            avance = self.env['plan_mejoramiento.avance'].search([
                ('accion_id', '=', vals['accion_id']),
                ('fecha_creacion', '>=', fecha_inicio),
                ('fecha_creacion', '<=', fecha_fin),
            ])
            if len(avance) >= 1:
                raise Warning('Solo se permite un avance por periodo de registro')

        # Campo aprobación jefe Unidad
        accion_select = self.env['plan_mejoramiento.accion'].browse([vals['accion_id']])
        es_jefe_dependencia = accion_select.jefe_dependencia_id.id == self.env.uid
        if vals.get('aprobacion_jefe_dependencia', False) and not es_jefe_dependencia:
            raise AccessError('El Campo [Aprobación Jefe Unidad] solo lo puede diligenciar el usuario Jefe de la Unidad')

        avance = super(plan_mejoramiento_avance, self).create(vals)
        return avance

    @api.one
    def write(self, vals):
        # Se valida que los avances ya calificados no sean modificados
        es_ejecutor = self.env.user.has_group_v8('plan_mejoramiento.ejecutor')[0]
        if len(vals) == 1 and self.tipo_calificacion_id and es_ejecutor:
            raise AccessError('No se permite modificar un avance que ya ha sido calificado')

        # Se valida que solo el jefe_dependencia apruebe el avance
        es_jefe_dependencia = self.accion_id.jefe_dependencia_id.id == self.env.uid
        if 'aprobacion_jefe_dependencia' in vals and not es_jefe_dependencia:
            raise AccessError('El Campo [Aprobación Jefe Unidad] solo lo puede diligenciar el usuario Jefe de la Unidad')

        # Se valida que el usuario auditor solo pueda realizar la calificación una vez este aprobado el avance por el usuario jefe_dependencia
        es_auditor = self.env.user.has_group_v8('plan_mejoramiento.auditor')[0]
        if ('tipo_calificacion_id' in vals or 'porcentaje' in vals) and es_auditor and self.aprobacion_jefe_dependencia == False:
            raise AccessError('Se podrá calificar este avance hasta que el usuario Jefe Depedencia lo apruebe')

        result = super(plan_mejoramiento_avance, self).write(vals)
        return result
