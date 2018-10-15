# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_hallazgo(common.TransactionCase):
    def test_date_max_min_halazgo_validaciones(self):
        _logger.info("\n***** test_date_max_min_halazgo_validaciones *****")
        """
            Se valida que la fecha Inicio y Fin del Hallazgo este dado
            Por la fecha minima y fecha maxima entre todas las acciones que
            pertenesca al hallazgo
        """

        plan_id = self.ref('plan_mejoramiento.id_plan_i_01')
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        ejecutor_oas_id = self.ref('plan_mejoramiento.id_user_ejecutor_oas')
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        # Crear Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(auditor_id).create({
            'plan_id': plan_id,
            'name': 'Hallazgo Test 01',
            'descripcion': 'Descripción de Hallazgo Interno 01',
            'proceso_id' : self.ref('operacion_por_procesos.mapa_proceso_proceso_7'),
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'state': 'en_progreso',
            'user_id': auditor_id,
        })
        # Crear Accion
        accion_01 = self.env['plan_mejoramiento.accion'].sudo(ejecutor_oas_id).create({
            'name': 'accion Interna 01',
            'descripcion': 'Descripción Acción Interna Preventiva de ...',
            'tipo': 'preventivo',
            'state': 'nuevo',
            'ejecutor_id': ejecutor_oas_id,
            'hallazgo_id': hallazgo.id,
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'objetivo': 'Objetivo de accion Interna',
            'indicador': 'tareas asignadas/tareas resueltas',
            'unidad_medida': 'tareas resueltas',
            'meta': 'lograr realizar...',
            #'recurso_ids': [id_recusro_01,],
            'fecha_inicio': today - timedelta(days=10),
            'fecha_fin': today + timedelta(days=10),
        })
        accion_02 = self.env['plan_mejoramiento.accion'].sudo(ejecutor_oas_id).create({
            'name': 'accion Interna 02',
            'descripcion': 'Descripción Acción Interna Preventiva de ...',
            'tipo': 'preventivo',
            'state': 'nuevo',
            'ejecutor_id': ejecutor_oas_id,
            'hallazgo_id': hallazgo.id,
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'objetivo': 'Objetivo de accion Interna',
            'indicador': 'tareas asignadas/tareas resueltas',
            'unidad_medida': 'tareas resueltas',
            'meta': 'lograr realizar...',
            #'recurso_ids': [id_recusro_01,],
            'fecha_inicio': today - timedelta(days=5),
            'fecha_fin': today + timedelta(days=20),
        })
        accion_03 = self.env['plan_mejoramiento.accion'].sudo(ejecutor_oas_id).create({
            'name': 'accion Interna 03',
            'descripcion': 'Descripción Acción Interna Preventiva de ...',
            'tipo': 'preventivo',
            'state': 'nuevo',
            'ejecutor_id': ejecutor_oas_id,
            'hallazgo_id': hallazgo.id,
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'objetivo': 'Objetivo de accion Interna',
            'indicador': 'tareas asignadas/tareas resueltas',
            'unidad_medida': 'tareas resueltas',
            'meta': 'lograr realizar...',
            #'recurso_ids': [id_recusro_01,],
            'fecha_inicio': today - timedelta(days=40),
            'fecha_fin': today + timedelta(days=40),
        })
        fecha_inicio = datetime.strptime(hallazgo.fecha_inicio,'%Y-%m-%d')
        fecha_fin  = datetime.strptime(hallazgo.fecha_fin,'%Y-%m-%d')
        date_min = today - timedelta(days=40)
        date_max = today + timedelta(days=40)

        if fecha_inicio != date_min or fecha_fin != date_max:
            self.fail('Error en la fecha Maxima y Minima del Hallazgo')

        # Campos computados
        self.assertEqual(
            fecha_inicio,
            date_min,
            'Error en el calculo de la Fecha inicio del Hallazgo'
        )
        self.assertEqual(
            fecha_fin,
            date_max,
            'Error en el calculo de la Fecha Fin del Hallazgo'
        )
        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()