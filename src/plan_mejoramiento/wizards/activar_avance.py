# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from openerp.exceptions import ValidationError, Warning
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openid import store
from duplicity.tempdir import default


class plan_mejoramientos_wizard_activar_avance(models.TransientModel):
    _name = 'plan_mejoramiento.wizard.activar_avance'

    def _default_fecha_inicio(self):
        fecha_max = self.env['plan_mejoramiento.parametro_activar_avance'].search([],
            order='create_date DESC',
            limit=1,
        )
        return fecha_max.fecha_inicio

    def _default_fecha_fin(self):
        fecha_max = self.env['plan_mejoramiento.parametro_activar_avance'].search([],
            order='create_date DESC',
            limit=1,
        )
        return fecha_max.fecha_fin

    # -------------------
    # Fields
    # -------------------
    fecha_inicio = fields.Date(
        string='Fecha Inicio',
        required=True,
        help='''Fecha inicio para registra avances''',
        default=_default_fecha_inicio,
    )
    fecha_fin = fields.Date(
        string='Fecha Fin',
        required=True,
        help='''Fecha fin para registrar avances''',
        default=_default_fecha_fin,
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
        if fecha_fin > tope:
            raise ValidationError('No se permite que la vigencia sea superior a un año')

    @api.one
    def _check_fechas(self):
        if(self.fecha_inicio and self.fecha_fin and
           self.fecha_inicio > self.fecha_fin
            ):
            raise ValidationError("Fecha de inicio no puede ser posterior a la de finalización")

    @api.multi
    def activar_avance(self):
        if (self.fecha_inicio and self.fecha_fin):
            self.env['plan_mejoramiento.parametro_activar_avance'].create({
                    'fecha_inicio': self.fecha_inicio,
                    'fecha_fin': self.fecha_fin,
            })
        return {'type': 'ir.actions.act_window_close'}


